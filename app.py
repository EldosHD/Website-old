#!/usr/bin/python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/secret/')
def secret():
    return '<p>you found me <br /> ~nyaa </p>'
