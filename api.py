from flask import Blueprint, jsonify, request, Markup, render_template
from .models import *
from flask_login import login_required, current_user
from . import db


api = Blueprint('api', __name__)
month_translations = ["Январь",
                    "Февраль",
                    "Март",
                    "Апрель",
                    "Май",
                    "Июнь",
                    "Июль",
                    "Август",
                    "Сентябрь",
                    "Октябрь",
                    "Ноябрь",
                    "Декабрь"]

@api.route('/api/get_user')
@login_required
def get_user():
    if request.args.get("user_id"):
        user_id = int(request.args.get("user_id"))
        user = User.query.get(user_id)
        if user:
            return jsonify({"status": True, "data": {
                "user_id": user.id,
                "f_name": user.f_name,
                "l_name": user.l_name,
                "gender": user.gender,
                "birthday": user.birthday,
                "nickname": user.nickname
            }})
        else:
            return jsonify({"status": "False", "data": "No such user"})
    else:
        return jsonify({"status": False, "data": "user_id is invalid"})


@api.route('/api/create_post', methods=["POST"])
@login_required
def create_post():
    post_text_final = Markup.striptags(request.form.get(
        "post_text"))
    p = Post(text=post_text_final, owner_id=current_user.id)
    db.session.add(p)
    db.session.commit()

    return jsonify({"status": True, "data": render_template("post.html", posts=[(p.id, p.text, p.publish_time, p.author.f_name)], month_translations=month_translations)})


@api.route('/api/get_user_posts')
@login_required
def get_user_posts():
    if request.args.get("user_id"):
        user_id = int(request.args.get("user_id"))
        user = User.query.get(user_id)
        if user:
            posts = [(post.id, post.text, post.publish_time, post.author.f_name) for post in user.posts.all()]
            return jsonify({"status": True, "data": posts})
        else:
            return jsonify({"status": False, "data": "No such user"})
    else:
        return jsonify({"status": False, "data": "User id is invalid"})


@api.route('/api/load_posts_for_user')
@login_required
def load_posts_for_user():
    posts = [(post.id, post.text, post.publish_time, post.author.f_name)
             for post in Post.query.all()]
    posts = reversed(posts)
    post_html = render_template("post.html", posts=posts, month_translations=month_translations)
    return jsonify({"status": True, "data": post_html})
