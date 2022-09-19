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
    school_number = db.Column(db.Integer)
    avatar_path = db.Column(db.String(100), default="default.png")
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    reactions = db.relationship('PostReactions', backref='user', lazy='dynamic', primaryjoin="User.id == PostReactions.user_id")
    comments = db.relationship('PostComments', backref='user', lazy='dynamic', primaryjoin="User.id == PostComments.user_id")

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(9000))
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    publish_time = db.Column(db.DateTime, default=datetime.now)
    privacy = db.Column(db.Integer, default=0)
    source_code_attachment = db.Column(db.String(9000))
    reactions = db.relationship('PostReactions', backref='author', lazy='dynamic')
    comments = db.relationship('PostComments', backref='post', lazy='dynamic')

class PostReactions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reaction_type = db.Column(db.Integer)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class PostComments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1000))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    