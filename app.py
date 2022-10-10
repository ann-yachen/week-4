# WeHelp Assignment: Week-4
# Python Flask

# Import Flask and related modules
from flask import Flask, request, redirect, url_for, render_template, session
import os # for secret key

# Create Application object
# "public" folder and "/" path for static files
app = Flask(__name__, static_folder = "public", static_url_path = "/")
app.secret_key = os.urandom(16) # random string to generate secret key

# username: test, password: test
user_test = {"username": "test", "password": "test"}

# Request-1, 2, 3
# Handle route "/" as homepage
@app.route("/")
def index():
    return render_template("index.html")

# Handle route "/signin" for form
@app.route("/signin", methods = ["POST"])
def signin():
    # get username and password from form by POST
    username = request.form.get("username")
    password = request.form.get("password")

    # if match to username and password in user_test
    if username == user_test["username"] and password == user_test["password"]:
        session["user"] = username # save username in session
        return redirect("/member") # redirect to /member
    # if username or password without input
    elif (username == "" or password == ""): 
        return redirect("/error?message=請輸入帳號、密碼") # redirect to /error with query string
    # if username or password is wrong
    else:
        return redirect("/error?message=帳號、或密碼輸入錯誤") # redirect to /error with query string

# Handle route "/member"
@app.route("/member")
def member():
    # if user has signed in
    if ("user" in session and session["user"] == user_test["username"]):
        return render_template("member.html")
    else:
        return redirect("/") # if not, redirect to homepage

# Handle route "/error"
@app.route("/error")
def error():
    # get query string of message
    message = request.args.get("message")
    # show message in error page
    return render_template("error.html", show_message = message)

# Handle route "/signout"
@app.route("/signout")
def signout():
    # delete user from session
    session.pop("user")
    return redirect("/") # redirect to homepage after signout

# Request-4 (Optional)
# Handle route "/square"
@app.route("/square")
def square():
    # get number from form and pass to calculate_square()
    input_number = request.args.get("number")
    return redirect(url_for("calculate_square", number = input_number))

# Handle route "/square/<number>", display URL as /square/input_number
@app.route("/square/<number>")
def calculate_square(number):
    number = int(number)
    result = number * number # calculate number * number (square)
    return render_template("square.html", show_result = result)

# Run server, port set as 3000
app.run(port = 3000) # http://127.0.0.1:3000/