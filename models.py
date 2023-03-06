from flask_login import UserMixin
from __init__ import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    music = db.Column(db.String(1000))
    toDo1 = db.Column(db.String(1000))
    toDo2 = db.Column(db.String(1000))
    toDo3 = db.Column(db.String(1000))
    toDo4 = db.Column(db.String(1000))
    toDo5 = db.Column(db.String(1000))
