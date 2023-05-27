from dotenv import load_dotenv
import os 

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_ORGANIZATION_ID = os.environ.get("OPENAI_ORGANIZATION_ID")
PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
PINECONE_ENV = os.environ.get("PINECONE_ENV")