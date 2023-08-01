from db_connector.mongo_db import  MongoConnector
from utils.constant import DB_NAME, USER_COLLECTION
import time
from passlib.hash import bcrypt_sha256

def UserSignUp(email, password):
    db = MongoConnector()
    db_client = db.loadCollections(DB_NAME, USER_COLLECTION)
    user_record = db_client.find_one({"email":email})
    print("user_record:", user_record)
    if user_record is None:
        # new user creation
        user_data = { 
            "email": email, 
            "password": bcrypt_sha256.hash(password),
            "created_at": int(time.time()),
            "updated_at": int(time.time()),
        }
        db_client.insert_one(user_data)

        return True
    else:
        # user already exists
        return False

        # bcrypt_sha256.verify(post_password, password)