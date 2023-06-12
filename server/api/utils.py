from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA, retrieval_qa
from langchain.vectorstores.pinecone import Pinecone
from langchain.embeddings import OpenAIEmbeddings
from typing import Any 
import pinecone
import os

def chat_with_webpage(db:Pinecone,query:str,OPENAI_API_KEY=None) -> str:
    """ chat with stored url data in pinecone"""
    
    if not OPENAI_API_KEY:
        OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

    retriever = db.as_retriever(search_type="similarity", search_kwargs={"k":2}) # db retriever
    llm=ChatOpenAI(model_name="gpt-3.5-turbo",openai_api_key=OPENAI_API_KEY) # OpenAI(openai_api_key=self.OPENAI_API_KEY)

    qa_chain = RetrievalQA.from_chain_type(
            llm=llm,chain_type="stuff", retriever=retriever) # chain_type: map_reduce, refine, map-rerank
    
    chain_out = qa_chain.run(query)
    print(chain_out)
    # return {"Answer":chain_out["answer"], "Source":chain_out["sources"]} 
    return {"Answer":chain_out} 


def load_existing_database(OPENAI_API_KEY=None,PINECONE_INDEX="aboneda") -> Pinecone:
    """Get a connection with pinecone index inwhich the url data is stored"""

    if os.environ.get("PINECONE_INDEX"):
        PINECONE_INDEX = os.environ.get("PINECONE_INDEX")

        embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
        db = Pinecone.from_existing_index(index_name=PINECONE_INDEX,embedding=embeddings)
        return db
