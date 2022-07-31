from crypt import methods
from flask import Blueprint, request, jsonify, make_response, abort
from sqlalchemy import func
from app import db
from app.models.user import User
from .post_routes import Post
from .pet_routes import Pet

user_bp = Blueprint('user_bp', __name__, url_prefix='/users')


#Validation
def validate_user(user_id):
    try:
        user_id=int(user_id)
    except:
        abort(make_response({'details': f'user {user_id} invalid'}), 400)

    user = User.query.get(user_id)

    if not user:
        abort(make_response({'details': f'user {user_id} does not exist'}, 404))
    return user

#GET user
@user_bp.route('/<user_id>', methods =['GET'])
def get_user(user_id):
    user= validate_user(user_id)
    return jsonify(user.to_dict()), 200

#Create a Post
@user_bp.route('/<user_id>/post', methods =['POST'])
def create_post(user_id):
    user = validate_user(user_id)

    request_body= request.get_json()
    new_post=Post(
        title=request_body['title'],
        description=request_body['description'],
        image=request_body['image'],
        pet_id=request_body['pet_id'],
        is_claim=request_body['is_claim'],
        reference_post_id=request_body['reference_post_id']
        )

    db.session.add(new_post)
    user.post.append(new_post)
    db.session.commit()

    return jsonify({
        'post_id': new_post.post_id,
        'title': new_post.title,
        'image':new_post.image,
        'pet_id':new_post.pet_id,
        'user_id': user.user_id,
        'is_claim':new_post.is_claim,
        'reference_post_id':new_post.reference_post_id
    }), 201

#GET all pets from user
@user_bp.route('/<user_id>/pets', methods =['GET'])
def get_user_pets(user_id):
    user = validate_user(user_id)

    pets_response =[]
    for pet in user.pets:
        pets_response.append(pet.to_dict())
    
    return jsonify({
        'user_id':user.user_id,
        'name':user.name,
        'pets':pets_response
        }), 200
  
