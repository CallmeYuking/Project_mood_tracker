from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()


class User(db.Model):
    """User information."""

    __tablename__ = "user"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    gender = db.Column(db.String(20))
    email = db.Column(db.String(150), unique=True, nullable=False)
    image_file = db.Column(db.String(50),
                           nullable=False,
                           default='/static/default.img')
    password = db.Column(db.String(50), nullable=False)
    birthday = db.Column(db.String(30), nullable=False)
    
    posts = db.relationship('Post', backref='author')
    moodrecords = db.relationship('Moodrecord', backref='author')

    def __repr__(self):
        return f"""(User username={self.username}
                         useremail={self.email}
                         image_file={self.image_file})"""



class Moodrecord(db.Model):
    """User daily mood record."""

    __tablename__ = "moodrecord"

    id = db.Column(db.Integer, primary_key=True)
    wake_up_time = db.Column(db.Text, nullable=False)
    sleep_efficiency = db.Column(db.Text)
    weather = db.Column(db.Text)
    meal = db.Column(db.Text)
    exercise = db.Column(db.Text)   
    mood_evaluate = db.Column(db.Text, nullable=False)
    notes = db.Column(db.Text)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"""(Moodrecord wake_up_time={self.wake_up_time}
                               sleep_efficiency={self.sleep_efficiency}
                               weather={self.weather}
                               meal={self.meal}
                               exercise={self.exercise}
                               mood_evaluate={self.mood_evaluate}
                               notes={self.notes}
                )"""

class Post(db.Model):
    """User post"""

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"""(Posts title={self.title}
                         date={self.date_posted})"""


def connect_to_db(app):

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///mood_tracker"

    db.app = app
    db.init_app(app)

    print("Connect to mood_tracker database")


if __name__ == '__main__':
    from mood_tracker import app

    connect_to_db(app)