from flask import Blueprint, jsonify, request, Markup
from .models import *
from flask_login import login_required, current_user
from . import db


api = Blueprint('api', __name__)
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
    p = Post(text=Markup.striptags(request.form.get("post_text")), owner_id=current_user.id)
    db.session.add(p)
    db.session.commit()

    return jsonify({"status": True})

@api.route('/api/get_user_posts')
@login_required
def get_user_posts():
    if request.args.get("user_id"):
        user_id = int(request.args.get("user_id"))
        user = User.query.get(user_id)
        if user:
            posts = [(post.id, post.text) for post in user.posts.all()]
            return jsonify({"status": True, "data": posts})
        else:
            return jsonify({"status": False, "data": "No such user"})
    else:
        return jsonify({"status": False, "data": "User id is invalid"})