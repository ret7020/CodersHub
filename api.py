from flask import Blueprint, jsonify, request, Markup, render_template
from .models import *
from flask_login import login_required, current_user
from . import db
import json
from .utils import numeral_noun_declension

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
    source_code_attachment = request.form.get("post_attachment_code_snippet")
    if source_code_attachment:
        p.source_code_attachment = source_code_attachment
    db.session.add(p)
    db.session.commit()
    return jsonify({"status": True, "data": render_template("post.html", posts=[(p.id, p.text, p.publish_time, p.author.f_name, p.author.avatar_path, -1, "0 комментариев", source_code_attachment, 0)], month_translations=month_translations)})


@api.route('/api/get_user_posts')
@login_required
def get_user_posts():
    if request.args.get("user_id"):
        user_id = int(request.args.get("user_id"))
        user = User.query.get(user_id)
        if user:
            posts = [(post.id, post.text, post.publish_time, post.author.f_name, post.author.avatar_path) for post in user.posts.all()]
            return jsonify({"status": True, "data": posts})
        else:
            return jsonify({"status": False, "data": "No such user"})
    else:
        return jsonify({"status": False, "data": "User id is invalid"})


@api.route('/api/load_posts_for_user')
@login_required
def load_posts_for_user():
    posts = []
    for post in Post.query.all():
        reaction = post.reactions.filter(PostReactions.user_id == current_user.id).all()
        reactions_cnt = len(post.reactions.filter(PostReactions.reaction_type == 1).all())
        if reaction:
            reaction = reaction[0].reaction_type
        else:
            reaction = -1
        comments_cnt = len(post.comments.all())
        posts.append((post.id, post.text, post.publish_time, post.author.f_name, post.author.avatar_path, reaction, f'{comments_cnt} {numeral_noun_declension(comments_cnt, "комментарий", "комментария", "комментариев")}', post.source_code_attachment, reactions_cnt))
    #posts = [(post.id, post.text, post.publish_time, post.author.f_name, post.author.avatar_path, post.reactions.filter(PostReactions.user_id == current_user.id).all())
    #         for post in Post.query.all()]
    posts = reversed(posts)

    post_html = render_template("post.html", posts=posts, month_translations=month_translations, user_avatar=current_user.avatar_path)
    return jsonify({"status": True, "data": post_html})

@api.route('/api/react_post', methods=['POST'])
@login_required
def react_post():
    data = json.loads(request.data.decode("utf-8"))
    if 'post_id' in data:
        post = Post.query.get(data['post_id'])
        if post:
            reacted = None
            for reaction in post.reactions.all():
                if reaction.user_id == current_user.id:
                    reacted = reaction
            if not reacted:
                if "reaction_type" in data and data["reaction_type"] in [0, 1]:
                    new_reaction = PostReactions(reaction_type=data["reaction_type"], post_id=data['post_id'], user_id=current_user.id)
                    db.session.add(new_reaction)
                    db.session.commit()
                else:
                    return jsonify({"status": False, "data": "Invalid reaction type"})
            else:
                if reacted.reaction_type == data['reaction_type']:
                    db.session.delete(reacted)
                else:
                    reacted.reaction_type = data['reaction_type']
                    db.session.add(reacted)
                db.session.commit()
            return jsonify({"status": True})
        else:
            return jsonify({"status": False, "data": "No such post"})
    else:
        return jsonify({"status": False, "data": "Invalid post_id"})