from db_connector.mongo_db import  MongoConnector
from utils.constant import DB_NAME, USER_COLLECTION
import time
from passlib.hash import bcrypt_sha256

def UserLogin(email, password):
    db = MongoConnector()
    db_client = db.loadCollections(DB_NAME, USER_COLLECTION)
    user_record = db_client.find_one({"email":email})
    print("user_record:", user_record)

    if user_record is None:
        # user doest exist
        return False
    else:
        # user exists
        if bcrypt_sha256.verify(password, user_record["password"]):
            return True
        else:
            return False
        