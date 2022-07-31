from crypt import methods
from flask import Blueprint, request, jsonify, make_response, abort
from sqlalchemy import func
from app import db
from app.models.pet import Pet
from .user_routes import User

pet_bp = Blueprint('pet_bp', __name__, url_prefix='/pets')


#Validation
def validate_pet(pet_id):
    try:
        pet_id=int(pet_id)
    except:
        abort(make_response({'details': f'Pet {pet_id} invalid'}), 400)

    pet = Pet.query.get(pet_id)

    if not pet:
        abort(make_response({'details': f'Pet {pet_id} does not exist'}, 404))
    return pet

#GET one pet
@pet_bp.route('/<pet_id>', methods =['GET'])
def get_user_pets(pet_id):
    pet=validate_pet(pet_id)
    return jsonify(pet.to_dict()), 200

#update pet 
@pet_bp.route('/<pet_id>', methods =['PATCH'])
def update_post(pet_id):
    pet=validate_pet(pet_id)
    request_body=request.get_json()
    pet.name=request_body['name']
    pet.detail=request_body['detail']
    pet.photo=request_body['photo']
    pet.type=request_body['type']
    pet.user_id=request_body['user_id']
    
    db.session.commit()
    return jsonify(f'Pet {pet_id} updated'), 200

#Delete Pet
@pet_bp.route('/<pet_id>', methods =['DELETE'])
def delete_pet(pet_id):
    pet=validate_pet(pet_id)
    
    db.session.delete(pet)
    db.session.commit()

    return{'details': f'Pet {pet_id} was successfully deleted'}, 200

