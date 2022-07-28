from app import db

class User(db.Model):
    user_id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String)
    location = db.Column(db.String)
    posts= db.relationship('Post', back_populates='user', lazy=True)
    pets= db.relationship('Pet', back_populates='user', lazy=True)

def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location
        }