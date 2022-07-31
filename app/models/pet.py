from app import db

class Pet(db.Model):
    pet_id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    pet_name = db.Column(db.String)
    detail = db.Column(db.String)
    photo = db.Column(db.bytea)
    posts= db.relationship('Post', back_populates='pet', lazy=True)
    user_id = db.Colummn(db.Integer, db.ForeingKey('user.user_id'), nullable=False)
    user = db.relationship('User', back_populates='user', lazy=True)

def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'detail': self.detail,
            'photo':self.photo,
            'type':self.type
        }