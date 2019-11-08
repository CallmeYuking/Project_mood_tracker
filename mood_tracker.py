
from flask import Flask, render_template, redirect, request, session
from model import db


app = Flask(__name__)


@app.route('/')
def show_homepage():
    """Show homepage for user."""

    if 'name' in session:
        return redirect('/user-homepage.html')
    


    return render_template('homepage.html')


@app.route('/get-name')
def get_name():
    """Get name from homepage form and store name in session."""

    return render_template('/registration.html')


@app.route('/user-homepage')
def show_user_homepage():
    """Show user's homepage including: user profile and main feature."""
    pass

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(host='0.0.0.0', debug=True)