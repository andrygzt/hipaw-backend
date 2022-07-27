from app import db

class User(db.Model):
    user_id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String)
    location = db.Column(db.String)
    post_id = db.Column(db.Integer, db.ForeignKey('post.post_id'), nullable=True)
    post= db.relationship('Post', back_populates='user', lazy=True)
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.pet_id'), nullable=False)
    pet= db.relationship('Pet', back_populates='user', lazy=True)

def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location
        }