#!/usr/bin/python3
"""This is the code for my amazing website."""

from flask import Flask, render_template, redirect, url_for, session, request
from flask import flash
from datetime import timedelta

app = Flask(__name__)
app.permanent_session_lifetime = timedelta(days=5)


@app.route('/')
@app.route('/home/')
def home():
    return render_template('index.html')


@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
