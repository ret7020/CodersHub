from flask import Blueprint, render_template, redirect
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    if current_user.is_authenticated:
        return redirect('/feed')
    else:
        return render_template('login.html')

@main.route('/feed')
@login_required
def feed():
    user_name = "Stephan"
    user_ava_path = '/users_data/avatars/default.png'
    return render_template('feed.html', user_name=current_user.f_name, avatar_path=user_ava_path)

