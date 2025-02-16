########################################################################################
######################          Import packages      ###################################
########################################################################################
from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from __init__ import create_app, db

########################################################################################
# our main blueprint
main = Blueprint('main', __name__)

@main.route('/') # home page that return 'index'
def index():
    return render_template('index.html')

@main.route('/profile') # profile page that return 'profile'
@login_required
def profile():
    return render_template('profile.html', name=current_user.name, id=current_user.id, music=current_user.music, toDo1=current_user.toDo1, toDo2=current_user.toDo2, toDo3=current_user.toDo3, toDo4=current_user.toDo4, toDo5=current_user.toDo5)

@main.route('/singup') # profile page that return 'profile'
def signup():
    return render_template('signup.html')

@main.route('/login') # profile page that return 'profile'
def login():
    return render_template('login.html')

@main.route('/change')
def change():
    return render_template('change.html', name=current_user.name, id=current_user.id, music=current_user.music, toDo1=current_user.toDo1, toDo2=current_user.toDo2, toDo3=current_user.toDo3, toDo4=current_user.toDo4, toDo5=current_user.toDo5)


app = create_app() # we initialize our flask app using the __init__.py function
if __name__ == '__main__':
    with app.app_context():
        db.create_all() # create the SQLite database
    app.run(debug=True) # run the flask app on debug mode