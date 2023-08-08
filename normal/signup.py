from db_connector.mongo_db import  MongoConnector
from utils.constant import DB_NAME, USER_COLLECTION
from utils.validation import is_valid_email, is_valid_password
import time
from passlib.hash import bcrypt_sha256


class UserSignUp():

    def __init__(self, username, email, password):
        self.username = username
        self.email = email 
        self.password = password

        # self.dbConnect()
    
    def dbConnect(self):
        db = MongoConnector()
        self.db_client = db.loadCollections(DB_NAME, USER_COLLECTION)

    def dbClose(self):
        self.db_client.close()

    def validate(self):
        print("validate")
        if self.email is None or self.password is None:
            print("not validate")
            return {
                "message": "Email or password is missing",
            }, 404

        if not is_valid_email(self.email):
            return {
                "message": "Email is not valid",
            }, 400
        
        if not is_valid_password(self.password):
            return {
                "message": "Password is not strong",
            }, 400
        
        return self.checkUser()

    def checkUser(self):
        user_record = None
        # user_record = self.db_client.find_one({"email": self.email})
        print("user_record:", user_record)
        if user_record is None:
            # # new user creation
            # user_data = { 
            #     "username": self.username,
            #     "email": self.email, 
            #     "password": bcrypt_sha256.hash(self.password),
            #     "created_at": int(time.time()),
            #     "updated_at": int(time.time()),
            #     "active": False, # enable to true when verify with activation link
            #     "deleted": False,
            #     "blocked": False,
            #     # "blocked_reason": "",
            #     # "password_reset_at": 0,
            #     # "last_login_at": 0,
            #     # "verify_code": "",
            # }
            # self.db_client.insert_one(user_data)

            # self.sendActivation()

            return {
                "message": "Signup successful",
            }, 200
        else:
            # user already exists
            return {
                "message": "Account already associated with this email",
            }, 409

            # bcrypt_sha256.verify(post_password, password)

    def sendActivation(self):
        # To verify - send action link to signup email 
        pass


