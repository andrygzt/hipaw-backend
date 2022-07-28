from app import db

class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True, autoincrement =True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    image = db.Column(db.bytea)
    users = db.relationship('User', back_populates='posts', lazy=True)
    pet= db.relationship('Pet', back_populates='posts', lazy=True)
    pet_id = db.Column(db.Integet, db.ForeingKey('pet.pet_id'), nullable=False)
    reference_post_id = db.Colummn(db.Integer, db.ForeingKey('post.post_id'), nullable=True)
    reference_post = db.relationship('Post', back_populates='post', lazy=True)