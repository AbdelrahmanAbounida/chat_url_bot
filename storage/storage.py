"""
Store url data to pinecone
"""


from langchain.document_loaders import UnstructuredURLLoader # Load webpages urls
from langchain.text_splitter import CharacterTextSplitter # text splitter 
from langchain.embeddings import OpenAIEmbeddings



class Storage:
    def __init__(self,OPENAI_API_KEY:str,PINECONE_API_KEY:str,PINECONE_ENV:str):
        self.OPENAI_API_KEY = OPENAI_API_KEY
        self.PINECONE_API_KEY = PINECONE_API_KEY
        self.PINECONE_ENV = PINECONE_ENV