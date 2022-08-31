#!/usr/bin/python3
"""This is the code for my amazing website."""

from flask import Flask, render_template, redirect, url_for, session, request
from flask import flash
from datetime import timedelta
import argparse

app = Flask(__name__)
app.permanent_session_lifetime = timedelta(days=5)


@app.route('/')
@app.route('/home/')
def home():
    return render_template('index.html')


@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/projects/')
def projects():
    return render_template('projects.html')


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('--debug',action='store_true' ,default=False ,help='Enables debug mode for the flask')
    parser.add_argument('-p','--port',default=80, type=int ,help='Specify the port for the webserver')
    parser.add_argument('--test',action='store_true' ,default=False ,help='Sets debug mode to true and the port to 5000')

    args = parser.parse_args()
    
    if args.test == True:
        args.debug = True
        args.port = 5000

    app.run(debug=args.debug, port=args.port)
