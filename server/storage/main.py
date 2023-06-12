from storage.URLLoader import URLLoader
from storage.PineconeAgent import PineconeAgent
from dotenv import load_dotenv
import os 

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_ORGANIZATION_ID = os.environ.get("OPENAI_ORGANIZATION_ID")
PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
PINECONE_ENV = os.environ.get("PINECONE_ENV")
PINECONE_INDEX = os.environ.get("PINECONE_INDEX")


urls = ["https://python.langchain.com/en/latest/index.html"]

# 0- Required Tools
url_loader = URLLoader(URLS=urls)
pinecone_agent = PineconeAgent(OPENAI_API_KEY= OPENAI_API_KEY,
    PINECONE_API_KEY= PINECONE_API_KEY,
    PINECONE_ENV= PINECONE_ENV,
    PINECONE_INDEX_NAME= PINECONE_INDEX,
    OPENAI_ORGANIZATION_ID=OPENAI_ORGANIZATION_ID
    )

# 1- Initializing Pinecone Agent
print("\033[38;5;208m Initializing Pinecone \033[38;5;208m")
pinecone_agent.init_pinecone()
print("Done...\n")

# 2- Create an index in pinecone
print("\033[38;5;39m Creating Pinecone Index \033[38;5;39m")
pinecone_agent.create_pinecone_index()
print("Done...\n")

# 3- Get all nested urls
print("\033[38;5;226m Getting The webpage Urls \033[38;5;226m")
all_urls = url_loader.get_webpage_urls()
print("Done...\n")

# # 4- load data from these urls 
print("\033[0m  Loading Data from the urls \033[0m")
data = url_loader.load_urls_data(all_urls[0:3]) # just for testing
print("Done...\n")

# # 5- store data to pinecone 
print("\033[38;5;46m Storing data to pinecone \033[38;5;46m")
db = pinecone_agent.store_to_pinecone(data)
print("Now you are ready to start chatting with the url\n")

# # 6- Now we are ready to get back to the chat UI and send questions to the server
# query = "test"
# docs = db.similarity_search(query)
# print(docs[0].page_content)
# print("Done...\n")
