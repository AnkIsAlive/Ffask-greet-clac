from flask import Flask

app = Flask(__name__)


@app.route('/welcome')
# Returns Welcome Message #
def welcome_msg():
    return "Welcome!"


@app.route('/welcome/back')
# Returns Welcome Back Message #
def welcome_back_msg():
    return "Welcome back!"


@app.route('/welcome/home')
# Returns Welcome Home Message #
def welcome_home_msg():
    return "Welcome Home!"
