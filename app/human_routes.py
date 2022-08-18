from crypt import methods
from flask import Blueprint, request, jsonify, make_response, abort
from sqlalchemy import func
from app import db
from app.models.human import Human
from .post_routes import Post
from .pet_routes import Pet

human_bp = Blueprint('human_bp', __name__, url_prefix='/humans')


#Validation
def validate_human(human_id):
    try:
        human_id=int(human_id)
    except:
        abort(make_response({'details': f'human {human_id} invalid'}), 400)

    human = Human.query.get(human_id)

    if not human:
        abort(make_response({'details': f'Human {human_id} does not exist'}, 404))
    return human

#Create human
@human_bp.route('', methods =['POST'])
def create_human():
    request_body = request.get_json()
    new_human = Human(human_name=request_body['name'],
                    location=request_body['location'],
                    human_email=request_body['email'])

    db.session.add(new_human)
    db.session.commit()

    return make_response(f'New User: "{new_human.human_id}" succesfully created.  YAY!', 201)

#GET human
@human_bp.route('/<human_id>', methods =['GET'])
def get_human(human_id):
    human= validate_human(human_id)
    return jsonify(human.to_dict()), 200

#GET human by email
@human_bp.route('/email/<human_email>', methods =['GET'])
def get_human_by_email(human_email):
    human = Human.query.filter_by(human_email=human_email).first()
    return jsonify(human.to_dict() if human else None), 200

#Create a pet
@human_bp.route('/<human_id>/pet', methods =['POST'])
def create_pet(human_id):
    human = validate_human(human_id)
    request_body = request.get_json()
    new_pet = Pet(pet_name=request_body['name'],
                    detail=request_body['detail'],
                    type=request_body['type'],
                    age=request_body['age'],
                    size=request_body['size'],
                    human_id=human_id)

    db.session.add(new_pet)
    human.pets.append(new_pet)
    db.session.commit()

    return make_response(f'New Pet: "{new_pet.pet_name}" succesfully created.  YAY!', 201)

#Create a Post
@human_bp.route('/<human_id>/post', methods =['POST'])
def create_post(human_id):
    human = validate_human(human_id)

    request_body= request.get_json()
    if request_body['is_claim'] == False:
        request_body['reference_post_id']= None

    new_post=Post(
        title=request_body['title'],
        description=request_body['description'],
        pet_id=request_body['pet_id'],
        is_claim=request_body['is_claim'],
        category=request_body['category'],
        post_status="Active",
        reference_post_id=request_body['reference_post_id'],
        human_id=human_id
        )

    db.session.add(new_post)
    human.posts.append(new_post)
    db.session.commit()

    return jsonify({
        'post_id': new_post.post_id,
        'title': new_post.title,
        'image':new_post.image,
        'status':new_post.post_status,
        'pet_id':new_post.pet_id,
        'human_id': human.human_id,
        'category':new_post.category,
        'is_claim':new_post.is_claim,
        'reference_post_id':new_post.reference_post_id
    }), 201

#GET all pets from human
@human_bp.route('/<human_id>/pets', methods =['GET'])
def get_human_pets(human_id):
    human = validate_human(human_id)

    pets_response =[]
    for pet in human.pets:
        pets_response.append(pet.to_dict())
    
    return jsonify({
        'human_id':human.human_id,
        'name':human.human_name,
        'pets':pets_response
        }), 200

#GET all post from human
@human_bp.route('/<human_id>/posts', methods =['GET'])
def get_human_post(human_id):
    human = validate_human(human_id)

    posts_response =[]
    for post in human.posts:
        posts_response.append(post.to_dict())
    
    return jsonify({
        'human_id':human.human_id,
        'name':human.human_name,
        'peosts':posts_response
        }), 200


#Delete human
@human_bp.route('/<human_id>', methods =['DELETE'])
def delete_human(human_id):
    human=validate_human(human_id)
    
    db.session.delete(human)
    db.session.commit()

    return{'details': f'Human {human_id} was successfully deleted'}, 200