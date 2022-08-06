from flask import Flask
import os

app = Flask(__name__)

LICENSE = os.environ.get("LICENSE_KEY")

@app.route('/')
def hello_world():
    return 'Hello world',LICENSE

if __name__ == '__main__':
    app.run( debug=True, host="0.0.0.0")


# from flask import Flask

# app = Flask(__name__)


# @app.route('/')
# def hello():
#     return 'Hello, World!'
