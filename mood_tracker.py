
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


@app.route('/get-name', methods = ['GET'])
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



@app.route('/get-user-info', methods = ['GET', 'POST'])
def get_user_info():
    """Get user's information from register and update to database"""
    username = request.form.get('username')
    gender = request.form.get('')
    email = request.form.get('email')
    password = request.form.get('password')
    password1 = request.form.get('password1')
    month = request.form.get('month')
    day = request.form.get('day')
    year = request.form.get('year')
    birthday = f'{month} {day} {year}'
    # birthday = dateTime.date(month, day, year)
    new_user = User(username = username, gender = gender, email = email, password = password, birthday = birthday)

    if password != password1:
        flash("Password doesn't match! Please check again!")
        return render_template('/registration.html')
    else:
        db.session.add(new_user)
        db.session.commit()

        flash("You're successfully registered!")
        return redirect('/')
    

    


@app.route('/user-homepage')
def show_user_homepage():
    """Show user's homepage including: user profile and main feature."""
    pass

if __name__ == '__main__':
    connect_to_db(app)
    app.secret_key = 'super secret key'
    app.run(host='0.0.0.0', debug=True)