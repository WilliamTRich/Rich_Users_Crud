from flask_app import app
from flask import render_template, redirect, url_for, request
import flask_app
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

@app.route('/delete/<userID>')
def delete(userID):
    user = {'id' : userID}
    User.delete(user)
    return redirect('/users')

@app.route('/edit/<userID>', methods=['POST', 'GET'])
def edit(userID):
    if request.method == 'POST':
        data = {
            "id" : userID,
            "fname": request.form["fname"],
            "lname": request.form['lname'],
            "email": request.form['email']
        }
        User.edit(data)
        return redirect('/show/{}'.format(userID))
    else:
        return render_template('update_user.html')

@app.route('/show/<userID>')
def show_user(userID):
    user = {'id' : userID}
    userInfo = User.get_one(user)
    return render_template('show_user.html', user=userInfo )

@app.route('/create', methods=['POST'])
def create():
    data = {
        "fname": request.form["fname"],
        "lname": request.form['lname'],
        "email": request.form['email']
    }

    User.save(data)
    return redirect('/users')