
from flask import Flask, render_template
from model import db


app = Flask(__name__)

posts = [
        {
        'author': 'Erica',
        'title': 'mood record 1',
        'content': 'Today is a bad day!',
        'date_posted': 'Oct 30th, 2019'
        },
        {
        'author': 'Tiffany',
        'title': 'mood record 2',
        'content': 'Today is a good day!',
        'date_posted': 'Nov 31th, 2019'
        }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('homepage.html', posts=posts)



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)