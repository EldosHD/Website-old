#!/usr/bin/python3
"""This is the code for my amazing website."""

from flask import Flask, render_template, redirect, url_for, session, request
from flask import flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'test'    # TODOOOOOO: change to something secure
app.permanent_session_lifetime = timedelta(days=5)

favColor = '#FFFF33'


@app.route('/')
@app.route('/home/')
def home():
    if 'user' in session:
        return redirect(url_for('user'))
    else:
        return render_template('index.html', status='login')


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session.permanent = True
        user = request.form['username']
        session['user'] = user
        return redirect(url_for('user'))
    else:
        if 'user' in session:
            # only relevant, if the login page gets called manually
            # and when the user is already logged in
            return redirect(url_for('user'))
        return render_template('login.html', status='login')


@app.route('/logout/')
def logout():
    if 'user' in session:
        user = session['user']
        flash(f'{user} has been logged out successfully', 'info')
    session.pop('user', None)
    return redirect(url_for('login'))


@app.route('/user/')
def user():
    if "user" in session:
        # if logged in
        user = session['user']
        return render_template('user.html',
                               usr=user,
                               status='logout',
                               favColor=favColor
                               )
    else:
        return redirect(url_for('login'))


@app.route('/contact/')
def contact():
    if "user" in session:
        # if logged in
        return render_template('contact.html', status='logout')
    else:
        return render_template('contact.html', status='login')
