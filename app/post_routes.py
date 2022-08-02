from crypt import methods
from flask import Blueprint, request, jsonify, make_response, abort
from sqlalchemy import func
from app import db
from app.models.post import Post
from .human_routes import Human
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
    posts=Post.query.all()

    posts_response =[]
    for post in posts:
        posts_response.append(post.to_dict())
    return jsonify(posts_response), 200


#GET ONE post
@post_bp.route('/<post_id>', methods =['GET'])
def get_post(post_id):
    post= validate_post(post_id)
    return jsonify(post.to_dict()), 200

#Update a Post
@post_bp.route('/<post_id>', methods =['PATCH'])
def update_post(post_id):
    post=validate_post(post_id)
    request_body=request.get_json()
    post.title=request_body['title']
    post.description=request_body['description']
    post.pet_id=request_body['pet_id']
    post.human_id=request_body['human_id']
    
    db.session.commit()
    return jsonify(f'Post {post_id} updated'), 200

#update pet 
@post_bp.route('/<post_id>', methods =['PATCH'])
def upload(post_id):
    post=validate_post(post_id)
    post.image = request.files['image']
    db.session.commit()
    return jsonify(f'Post image updated'), 200

#Delete Post
@post_bp.route('/<post_id>', methods =['DELETE'])
def delete_post(post_id):
    post=validate_post(post_id)
    
    db.session.delete(post)
    db.session.commit()

    return{'details': f'Post {post_id} was successfully deleted'}, 200



