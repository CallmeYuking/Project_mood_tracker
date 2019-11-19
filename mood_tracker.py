
from flask import Flask, render_template, redirect, request, session, flash
from model import db, User, Post, Moodrecord, connect_to_db
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.secret_key = 'secret'


@app.route('/')
def show_homepage():
    """Show homepage for user."""

    if 'user_id' in session:
        return redirect('/user-homepage')
    
    return render_template('homepage.html')


@app.route('/register')
def register():
    """Register page for the new user."""
    
    return render_template('/registration.html')


@app.route('/get-name', methods=['POST'])
def get_name():
    """Get name from homepage form and store name in session."""

    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter(User.username == name, User.password == password).first()

    if user:
        session['user_id'] = user.id
        return render_template('user_homepage.html')
    else:
        flash('Username or password is wrong. Please check up again!')
        return render_template('homepage.html')



@app.route('/get-user-info', methods = ['GET', 'POST'])
def get_user_info():
    """Get user's information from register and update to database."""

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
    new_user = User(username = username,
                    gender = gender, 
                    email = email, 
                    password = password, 
                    birthday = birthday)

    # Check if password is matched:
    if password != password1:
        flash("Password doesn't match! Please check again!")
        return render_template('registration.html')
    else:
        db.session.add(new_user)
        db.session.commit()

        flash("You're successfully registered!")
        return redirect('/')
    

@app.route('/user-homepage', methods = ['GET'])
def show_user_homepage():
    """Show user's homepage including: user profile and main feature."""

    profile = request.args.get('profile')
    record = request.args.get('record')
    story = request.args.get('blog')
    world = request.args.get('world')

    if profile:
        return render_template('user_profile.html')
    elif record:
        return render_template('my_record.html')
    elif story:
        return render_template('my_story.html')

    return render_template('user_homepage.html')


@app.route('/get-user-record')
def show_add_record_form():
    """Render user's homepage and preventing user log in through route."""
    if 'user_id' in session:
        return render_template('my_record.html')

    return redirect('/')


@app.route('/get-user-record', methods=['POST'])
def get_user_record():
    """Get user's mood record and update to database."""

    wake_up_time = request.form.get('wakeup')
    sleep_efficiency = request.form.get('sleep')
    weather = request.form.get('weather')
    meal = request.form.get('meal')
    exercise = request.form.get('exercise')
    mood_evaluate = request.form.get('mood')
    notes = request.form.get('note')

    new_record = Moodrecord(wake_up_time = wake_up_time,
                            sleep_efficiency = sleep_efficiency,
                            weather = weather,
                            meal = meal,
                            exercise = exercise,
                            mood_evaluate = mood_evaluate,
                            notes = notes)
    # Add new_record to user that is currently logged in
    user_id = session['user_id']
    user = User.query.get(user_id)
    user.moodrecords.append(new_record)

    db.session.add(new_record)
    db.session.commit()

    flash("You've created a new mood record!")
    return redirect('/user-homepage')

@app.route('/get-user-story', methods = ['GET', 'POST'])
def get_user_story():
    """Get user's story and update to database."""

    title = request.form.get('title')
    content = request.form.get('content')

    user_story = Post(title = title,
                      content = content)

     # Add new_story to user that is currently logged in
    user_id = session['user_id']
    user = User.query.get(user_id)
    user.moodrecords.append(new_story)

    db.session.add(user_story)
    db.session.commit()

if __name__ == '__main__':
    connect_to_db(app)
    app.secret_key = 'super secret key'
    app.run(host='0.0.0.0', debug=True)






