from flask_login import UserMixin
from datetime import datetime
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    f_name = db.Column(db.String(1000))
    l_name = db.Column(db.String(1000))
    gender = db.Column(db.Integer)
    user_status = db.Column(db.Integer)
    birthday = db.Column(db.String(1000))
    nickname = db.Column(db.String(1000))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(9000))
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    publish_time = db.Column(db.DateTime, default=datetime.now)
    privacy = db.Column(db.Integer, default=0)

