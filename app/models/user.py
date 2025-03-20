from datetime import datetime
from flask_login import UserMixin
from app import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pubkey = db.Column(db.String(64), unique=True, nullable=False)
    name = db.Column(db.String(64))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # 关联房间操作记录
    room_operations = db.relationship('RoomOperation', backref='operator', lazy=True)
    
    def get_id(self):
        return self.pubkey
    
    @staticmethod
    def get_by_pubkey(pubkey):
        return User.query.filter_by(pubkey=pubkey).first()

class RoomOperation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    operation_type = db.Column(db.String(50), nullable=False)  # 'status_change', 'create', etc
    old_value = db.Column(db.String(200))
    new_value = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
