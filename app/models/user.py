from app import db

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    location = db.Column(db.String)
    post_id = db.relationship('Post', back_populates='user', lazy=True)
    pet_id = db.relationship('Pet', back_populates='user', lazy=True)

def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location
        }