from app import db

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(10), unique=True, nullable=False)
    type = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='available')  # available, occupied, maintenance
    
    def to_dict(self):
        return {
            'id': self.id,
            'number': self.number,
            'type': self.type,
            'price': self.price,
            'status': self.status
        }
