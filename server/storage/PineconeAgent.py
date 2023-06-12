"""
Store webpage data to pinecone
"""
from langchain.document_loaders import UnstructuredURLLoader # Load webpages urls
from langchain.text_splitter import CharacterTextSplitter # text splitter 
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
import pinecone
from typing import Any
class PineconeAgent:
    def __init__(self,OPENAI_API_KEY:str,OPENAI_ORGANIZATION_ID: str,PINECONE_API_KEY:str,PINECONE_ENV:str,PINECONE_INDEX_NAME:str):
        self.OPENAI_API_KEY = OPENAI_API_KEY
        self.OPENAI_ORGANIZATION_ID = OPENAI_ORGANIZATION_ID
        self.PINECONE_API_KEY = PINECONE_API_KEY
        self.PINECONE_ENV = PINECONE_ENV
        self.PINECONE_INDEX_NAME = PINECONE_INDEX_NAME

    def init_pinecone(self):
        pinecone.init(api_key=self.PINECONE_API_KEY, environment=self.PINECONE_ENV)
    
    def delete_index(self):
        pinecone.delete_index(self.PINECONE_INDEX_NAME)
    
    def create_pinecone_index(self):
        if not self.PINECONE_INDEX_NAME in pinecone.list_indexes():
            pinecone.create_index(self.PINECONE_INDEX_NAME,dimension=1536,metric="cosine")
            print(f"{self.PINECONE_INDEX_NAME} has been created")
            return 
    
    def store_to_pinecone(self,data:Any):
        # 1- Split the documents into chunks

        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        
        if type(data) == str:
            docs = text_splitter.create_documents([data])
        else:
            docs = text_splitter.split_documents(data)
        # 2- Creating Embedding Model
        embeddings = OpenAIEmbeddings(openai_api_key=self.OPENAI_API_KEY,openai_organization=self.OPENAI_ORGANIZATION_ID)

        # 3- Create the vectorstore to use as the index
        db = Pinecone.from_documents(docs,embeddings,index_name=self.PINECONE_INDEX_NAME)
        print("Document has been stored to pinecone successfully")  

        return db

    
    