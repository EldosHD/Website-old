#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<p>!False <br /> its funny cuz its true</p>"
