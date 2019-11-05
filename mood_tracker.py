from datetime import datetime 
from flask import Flask, render_template
from flask_sqlalchemy import SQLALchemy 
app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = ''

db = SQLALchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    fname = db.Column(db.String(15), nullable=False)
    lname = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    image_file = db.Column(db.String(20),nullable=False, default='default.img')
    password = db.Column(db.String(50), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.Datetime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"





@app.route('/')
def greeting():
    return render_template('homepage.html')




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)