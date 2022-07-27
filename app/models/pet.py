from app import db

class Pet(db.Model):
    pet_id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    pet_name = db.Column(db.String)
    detail = db.Column(db.String)
    post_id = db.Column(db.Integer, db.ForeingKey('post.post_id'), nullable=True)
    post= db.relationship('Post', back_populates='user', lazy=True)
    user_id = db.Colummn(db.Integer, db.ForeingKey('user.user_id'), nullable=False)
    user = db.relationship('User', back_populates='user', lazy=True)

def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'detail': self.detail
        }