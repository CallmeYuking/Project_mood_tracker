
from flask import Flask, render_template, redirect, request, session, flash
from model import db, User, Post, connect_to_db
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


@app.route('/')
def show_homepage():
    """Show homepage for user."""

    if 'name' in session:
        return redirect('/user-homepage.html')
    
    return render_template('homepage.html')


@app.route('/register')
def register():
    """Register page for the new user."""
    
    return render_template('/registration.html')


@app.route('/get-name', methods = ['get'])
def get_name():
    """Get name from homepage form and store name in session."""

    name = request.args.get('name')
    password = request.args.get('password')
    is_valid = User.query.filter(User.username == name, User.password == password).first()

    if is_valid:
        return render_template('/user-homepage.html')
    else:
        flash('Username or password is wrong. Please check up again!')
        return render_template('homepage.html')



@app.route('/get-user-info', methods = ['get', 'post'])
def get_user_info():
    """Get user's information from register and update to database"""
    username = request.args.get('username')
    gender = request.args.get('')
    email = request.args.get('email')
    password = request.args.get('password')
    birthday = request.args.get('month', 'day', 'year')


    

    pass


@app.route('/user-homepage')
def show_user_homepage():
    """Show user's homepage including: user profile and main feature."""
    pass

if __name__ == '__main__':
    connect_to_db(app)
    app.secret_key = 'super secret key'
    app.run(host='0.0.0.0', debug=True)