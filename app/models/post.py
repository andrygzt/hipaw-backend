from app import db


class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True, autoincrement =True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    image = db.Column(db.LargeBinary, nullable=True)
    category = db.Column(db.String)
    post_status = db.Column(db.String)
    human = db.relationship('Human', back_populates='posts', lazy=True)
    human_id = db.Column(db.Integer, db.ForeignKey('human.human_id'), nullable=False)
    pet= db.relationship('Pet', back_populates='posts', lazy=True)
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.pet_id'), nullable=False)
    is_claim=db.Column(db.Boolean, nullable=False)
    reference_post_id = db.Column(db.Integer, db.ForeignKey('post.post_id'), nullable=True)
    reference_post = db.relationship('Post', back_populates='claim', lazy=True)
    claim= db.relationship('Post', lazy=True)

    def to_dict(self):
        return {
            'id' : self.post_id,
            'category':self.category,
            'status':self.post_status,
            'title': self.title,
            'description': self.description,
            'image': f"posts/images/{self.post_id}.jpg",
            'pet_id': self.pet_id,
            'human_id': self.human_id,
            'is_claim':self.is_claim,
            'reference_port_id':self.reference_post_id,
        }
        