from app import db

class Pet(db.Model):
    pet_id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    pet_name = db.Column(db.String)
    detail = db.Column(db.String)
    photo = db.Column(db.LargeBinary, nullable=True)
    type = db.Column(db.String)
    posts= db.relationship('Post', back_populates='pet', lazy=True)
    human_id = db.Column(db.Integer, db.ForeignKey('human.human_id'), nullable=False)
    human = db.relationship('Human', back_populates='pets', lazy=True)
    age = db.Column(db.String)
    size = db.Column(db.String)

    def to_dict(self):
        return {
            'id': self.pet_id,
            'name': self.pet_name,
            'detail': self.detail,
            'photo':f"pets/images/{self.pet_id}.jpg",
            'type':self.type,
            'age': self.age,
            'size':self.size
        }