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
    return render_template('feed.html', user_name=current_user.f_name, avatar_path=f"/users_data/avatars/{current_user.avatar_path}")

@main.route('/faq')
@login_required
def faq_page():
    return render_template('full_text_page.html', user_name=current_user.f_name, avatar_path=f"/users_data/avatars/{current_user.avatar_path}", page_content='''<h2>CodersHub FAQ</h2>
    <ul>
        <li>Что это такое?</li>
        <i>Ответ</i>
        <li>Что это такое?</li>
        <i>Ответ</i>
        <li>Что это такое?</li>
        <i>Ответ</i>
        <li>Что это такое?</li>
        <i>Ответ</i>
        
    </ul>''')