from app import app
from flask import Flask

@app.route("/")
def hello():
    return "Hello World!"
