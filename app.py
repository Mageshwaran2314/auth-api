from flask import Flask, request, render_template
from normal.signup import UserSignUp
from normal.login import UserLogin
from utils.readenv import getEnvValue
from utils.constant import SITE_URL


app = Flask(
    __name__,
    static_url_path='', 
    # static_folder='web/static',
    template_folder='web/templates'
    )


@app.route("/")
def home():
    return "data"


@app.route('/signup')
def signup():
    print("SITE_URL:", SITE_URL)
    return render_template('signup.html', SITE_URL=getEnvValue(SITE_URL))


# recaptch validate in decorator
@app.route("/api/signup", methods=["POST"])
def signUpApi():
    try:
        post = request.json
        print("post:", post)
        username = post.get("username")
        email = post.get("email")
        password = post.get("password")

        print("email:", email)
        print("password:", password)
        signup = UserSignUp(username, email, password)

        data, code = signup.validate()
        return data, code
    except Exception as e:
        print("Error signup:", e)
        return {
            "message": "Something went wrong"
        }, 500


@app.route("/api/login", methods=["POST"])
def login():

    
    post = request.json
    isValid = UserLogin(post["email"], post["password"])

    
    if isValid :
        return "Login Success"
    else:
        return "Not valid user"


if __name__ == "__main__":
    app.run(debug=True)
