from crypt import methods
from flask import Blueprint, request, jsonify, make_response, abort
from sqlalchemy import func
from app import db
from app.models.pet import Pet
from .user_routes import User

pet_bp = Blueprint('pet_bp', __name__, url_prefix='/user_id')


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

#GET all pets from user
@pet_bp.route('/pets', methods =['GET'])
def get_user_pets():
    pets=Pet.query.all()

    pets_response =[]
    for pet in pets:
        pets_response.append(pet.to_dict())
    return jsonify(pets_response), 200