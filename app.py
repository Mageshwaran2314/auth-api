from flask import Flask, request
from db_connector.mongo_db import MongoConnector
from normal.signup import UserSignUp
from normal.login import UserLogin

from werkzeug.security import generate_password_hash,check_password_hash


app = Flask(__name__)
mongoConnector = MongoConnector()

@app.route("/")
def home():
     return "data"

@app.route("/api/signup", methods=["post"])
def signUp():
    post = request.json

    isValid = UserSignUp(post["email"], post["password"])

    if isValid :
        return "Please check your emial for verification link"
    else:
        return "Existing user"


@app.route("/api/login", methods=["post"])
def login():

    
    post = request.json
    isValid = UserLogin(post["email"], post["password"])

    
    if isValid :
        return "Login Success"
    else:
        return "Not valid user"


if __name__ == "__main__":
    app.run(debug=True)
           
        