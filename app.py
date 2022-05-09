#!/usr/bin/python3
"""This is the code for my amazing website."""

from flask import Flask, render_template, redirect, url_for, session, request
from flask import flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'test'    # TODOOOOOO: change to something secure
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # removes some warnings
app.permanent_session_lifetime = timedelta(days=5)

db = SQLAlchemy(app)


class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)  # defines the id and sets it as the primary_key
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email


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
    session.pop('email', None)
    return redirect(url_for('login'))


@app.route('/user/', methods=['POST', 'GET'])
def user():
    email = None
    if "user" in session:
        # if logged in
        user = session['user']
        if request.method == "POST":
            email = request.form['userEmail']
            session['email'] = email
            flash('Email was saved!', 'info')  # doesnt work rn. See login.html for info
        else:
            if 'email' in session:
                email = session['email']
        return render_template('user.html',
                               usr=user,
                               status='logout',
                               favColor=favColor,
                               email=email
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


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
