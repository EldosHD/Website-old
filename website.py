#!/usr/bin/python3
"""This is the code for my amazing website."""
from flask import Flask, render_template, redirect, url_for, session, request
from datetime import timedelta
import argparse
import owo

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

@app.route('/owo/')
@app.route('/uwu/')
@app.route('/translator/')
def translator():
    return render_template('translator.html')

