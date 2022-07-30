from crypt import methods
from flask import Blueprint, request, jsonify, make_response, abort
from sqlalchemy import func
from app import db
from app.models.user import User
from .post_routes import Post
from .pet_routes import Pet

user_bp = Blueprint('user_bp', __name__, url_prefix='/user_id')


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
@user_bp.route('', methods =['GET'])
def get_user(user_id):
    user= validate_user(user_id)
    return jsonify(user.to_dict()), 200