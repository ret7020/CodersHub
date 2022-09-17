from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    f_name = db.Column(db.String(1000))
    l_name = db.Column(db.String(1000))
    gender = db.Column(db.Integer)
    user_status = db.Column(db.Integer)
    birthdy = db.Column(db.String(1000))
    nickname = db.Column(db.String(1000))