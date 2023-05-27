"""
Load data from url
"""

from dotenv import load_dotenv
import os 
from typing import List 
import requests 
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from langchain.document_loaders import UnstructuredURLLoader
from langchain.document_loaders import PlaywrightURLLoader

from playwright.sync_api import sync_playwright
from unstructured.partition.html import partition_html

load_dotenv()

class URLLoader:
    def __init__(self,URLS:List[str]) -> None: 
        self.URLS = URLS

    def get_urls_sitemap(self,url:str) -> List[str]:
        """return all links in a given url using sitemap.xml""" 
        sitemap_url = url+"sitemap.xml"
        response = requests.get(sitemap_url)

        if response.status_code == 200:
            sitemap_content = response.text
            try:
                root = ET.fromstring(sitemap_content)
                pages = []
                for element in root.iter():
                    if 'loc' in element.tag:
                        pages.append(element.text)
                return pages 
            except Exception as e:
                print("************************************")
                print("Failed to get xmlsitemap conetnt")
                print(f"Error: {e}")
                print("************************************")
        return [""]
        
    def get_webpage_urls(self) -> List[str]:
        """return all urls in a page using sitemap or regular webscraping"""

        all_pages = []
        for url in self.URLS:
            # Method1: get urls using website sitemap
            all_urls = self.get_urls_sitemap(url)

            # Method2 : using regular web scraping
            if len(all_urls) <= 1: 
                reqs = requests.get(url)
                soup = BeautifulSoup(reqs.text, 'html.parser')

                print(reqs.text)
                all_urls = []

                for link in soup.find_all('a'):
                    all_urls.append(f"{url}{link.get('href')}")
            
            all_pages += all_urls
        
        return all_pages
    

    def manual_scraping(self,urls):
        """Test Method to try payright"""
            
        docs = list()
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            for url in urls:
                try:
                    page = browser.new_page()
                    page.goto(url)

                    page_source = page.content()

                    print(page_source)
                    elements = partition_html(text=page_source)
                    text = "\n\n".join([str(el) for el in elements])
                    docs.append(text)
                    
                except Exception as e:
                    if True:
                        print(
                            f"Error fetching or processing {url}, exception: {e}"
                        )
                    else:
                        raise e
            browser.close()
        return docs



if __name__ == '__main__':
    urls = ["https://parag-ritik.dkvdexjra0dxm.amplifyapp.com/"]

    url_loader = URLLoader(URLS=urls)

    # nest_urls = url_loader.get_webpage_urls()

    loader = PlaywrightURLLoader(urls=urls) # , remove_selectors=["header", "footer"]
    data = loader.load()

    print(data)