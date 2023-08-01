import pymongo
# from dotenv import load_dotenv
import os

from decouple import Config, RepositoryEnv

DOTENV_FILE = '.env'
env_config = Config(RepositoryEnv(DOTENV_FILE))



class MongoConnector:
    def __init__(self):
        print("aa")
        # url = os.getenv["MONGODB_URL"]
        MONGODB_URL = env_config.get('MONGODB_URL')
        try:
            self.client = pymongo.MongoClient(MONGODB_URL)
        except Exception as e: 
            print("error")
            raise e
        print(self.client)
    
    def close(self):
        self.client.close()

    def connect(self):
        return self.client   
    
    def loadDB(self,db_name):
        print("loaded")
        return self.client[db_name]

    def loadCollections(self,db_name,collection_name):
        return self.client[db_name][collection_name]   
    
    

