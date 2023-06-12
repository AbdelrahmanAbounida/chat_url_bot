from flask import Blueprint, request, Response, abort
from flask_restful import Api, Resource
from storage.URLLoader import URLLoader
from storage.PineconeAgent import PineconeAgent
from .utils import load_existing_database, chat_with_webpage
from dotenv import load_dotenv
from storage.PineconeAgent import PineconeAgent
from storage.URLLoader import URLLoader
import pinecone
import os 

# loading env variables
load_dotenv()
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_ORGANIZATION_ID = os.environ.get("OPENAI_ORGANIZATION_ID")
PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
PINECONE_ENV = os.environ.get("PINECONE_ENV")
PINECONE_INDEX = os.environ.get("PINECONE_INDEX")
FLASK_API_KEY = os.environ.get("FLASK_API_KEY")
# BASE_PROMPT = os.environ.get("BASE_PROMPT")


# initializae pinecone
pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)

# create index if not exist

# api initialization
chat_pb = Blueprint("UrlChatBot",__name__)
UrlChatBotAPI = Api(chat_pb)

# Open connection with pinecone vectordb (chatting)
vector_db = load_existing_database(OPENAI_API_KEY=OPENAI_API_KEY,PINECONE_INDEX=PINECONE_INDEX)

# pinecone agent connection (data storage)
pinecone_agent = PineconeAgent(OPENAI_API_KEY,OPENAI_ORGANIZATION_ID,PINECONE_API_KEY,PINECONE_ENV,PINECONE_INDEX)
pinecone_agent.init_pinecone()
pinecone_agent.create_pinecone_index()

# used for chatting
class UrlChatBot(Resource):
    def get(self):
        return "Url chatbot is working and ready for test"

    def post(self):
        
        if not 'API_KEY' in request.json:
            return Response('{"Error":"API_KEY must not be none"}',status=403, mimetype='application/json')
        
        if request.json['API_KEY'] != FLASK_API_KEY:
            return Response('{"Error":"API_KEY is not correct"}',status=403, mimetype='application/json')

        if not 'query' in request.json:
            return {"Error": "query field shouldn't be none"} 
        
        # start chatting
        query = request.json['query']
        try: 
            answer = chat_with_webpage(vector_db,query,OPENAI_API_KEY)
            return answer
        except Exception as e:
            print(f"Failed to get answer: {e}")

            # try to reinitialize pinecone connection
            try:
                pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)
                db = load_existing_database(OPENAI_API_KEY=OPENAI_API_KEY,PINECONE_INDEX=PINECONE_INDEX)
                answer = chat_with_webpage(db=db,query=query,OPENAI_API_KEY=OPENAI_API_KEY)
                return answer
            except Exception as e:
                print(e)
                return {"Error":f"Failed to get answer >> {e}"}

# used for storing data
class StorageBot(Resource):

    def get(self):
        return "This is Storage Bot"
    
    def post(self):
        if not 'API_KEY' in request.json:
            return Response('{"Error":"API_KEY must not be none"}',status=403, mimetype='application/json')
        
        if request.json['API_KEY'] != FLASK_API_KEY:
            return Response('{"Error":"API_KEY is not correct"}',status=403, mimetype='application/json')

        if not ('text' in request.json or 'url' in request.json):
            return {"Error": "You have to provide either a url or text data"}
        
        if 'text' in request.json:
            try:
                data = request.json['text']
                pinecone_agent.store_to_pinecone(data)
                return Response("{'Success':'Data has been stored successfully to pinecone'}", status=201, mimetype='application/json') 
            except Exception as e:
                print(e)
                return {"Error":f"Failed to store data to pinecone >> {e}"}
            

        if 'url' in request.json:
            try:
                max_urls = -1
                if 'max_urls' in request.json:
                    max_urls = int(request.json['max_urls'])

                url = request.json['url']
                url_loader = URLLoader(URLS=[url])
                
                if max_urls > 0:
                    all_urls = url_loader.get_webpage_urls()[0:max_urls]
                else:
                    all_urls = url_loader.get_webpage_urls()

                data = url_loader.load_urls_data(all_urls)
                db = pinecone_agent.store_to_pinecone(data)
                return Response("{'Success':'Url Data has been stored successfully to pinecone'}", status=201, mimetype='application/json') 
            except Exception as e:
                print(e)
                return {"Error":f"Failed to store data to pinecone >> {e}"}


class Test(Resource):
    def get(self):
        return "Test: Server is working"
    

# routing
UrlChatBotAPI.add_resource(UrlChatBot, '/chat')
UrlChatBotAPI.add_resource(StorageBot, '/store')
UrlChatBotAPI.add_resource(Test, '/')



