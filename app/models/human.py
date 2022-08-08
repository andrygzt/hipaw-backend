from app import db

class Human(db.Model):
    human_id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    human_name = db.Column(db.String)
    location = db.Column(db.String)
    posts= db.relationship('Post', back_populates='human', lazy=True)
    pets= db.relationship('Pet', back_populates='human', lazy=True)
    human_email = db.Column(db.String, nullable=True)

    def to_dict(self):
        return {
            'id': self.human_id,
            'name': self.human_name,
            'location': self.location,
            'email':self.human_email
        }