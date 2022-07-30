from crypt import methods
from flask import Blueprint, request, jsonify, make_response, abort
from sqlalchemy import func
from app import db
from app.models.post import Post
from .user_routes import User
from .pet_routes import Pet

post_bp = Blueprint('post_bp', __name__, url_prefix='/posts')


#Validation
def validate_post(post_id):
    try:
        post_id=int(post_id)
    except:
        abort(make_response({'details': f'post {post_id} invalid'}), 400)

    post = Post.query.get(post_id)

    if not post:
        abort(make_response({'details': f'post {post_id} does not exist'}, 404))
    return post

#GET all posts
@post_bp.route('', methods =['GET'])
def get_all_posts():
    posts=post.query.all()

    posts_response =[]
    for post in posts:
        posts_response.append(post.to_dict())
    return jsonify(posts_response), 200


#GET ONE post
@post_bp.route('/<post_id>', methods =['GET'])
def get_post(post_id):
    post= validate_post(post_id)
    return jsonify(post.to_dict()), 200



