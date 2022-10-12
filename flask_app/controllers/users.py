from flask_app import app
from flask import render_template, redirect, url_for, request
from flask_app.models.user import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users')
def users():
    return render_template('users_list.html', users=User.get_all())

@app.route('/create_user')
def create_user():
    return render_template('create_user.html')

@app.route('/create', methods=['POST'])
def create():
    data = {
        "fname": request.form["fname"],
        "lname": request.form['lname'],
        "email": request.form['email']
    }

    User.save(data)
    return redirect('/users')