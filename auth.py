from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User
from . import db

auth = Blueprint('auth', __name__)



@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password): 
        return jsonify({"status": False})

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return jsonify({"status": True})

@auth.route('/signup', methods=['POST'])
def signup_post():

    email = request.form.get('email')
    name = request.form.get('f_name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if user:
        return jsonify({"status": False, "error": "email"})

    new_user = User(email=email, f_name=name, password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()
    login_user(new_user, remember=True)

    return jsonify({"status": True})

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
