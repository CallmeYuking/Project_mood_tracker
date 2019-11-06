from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()


class User(db.Model):
    """User information."""

    __tablename__ = "user"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    fname = db.Column(db.String(15), nullable=False)
    lname = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    image_file = db.Column(db.String(20),nullable=False, default='default.img')
    password = db.Column(db.String(50), nullable=False)
    posts = db.relationship('Posts', backref='author')

    def __repr__(self):
        return f"""(User username={self.username}
                         useremail={self.email}
                         image_file={self.image_file})"""

class Posts(db.Model):
    """User post"""

    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    # date_posted = db.Column(db.Datetime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"""(Post title={self.title}
                         date={self.date_posted})"""


def connect_to_db(app):

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///mood_tracker.db"

    db.app = app
    db.init_app(app)

    print("Connect to mood_tracker database")


if __name__ == '__main__':
    from mood_tracker import app

    connect_to_db(app)