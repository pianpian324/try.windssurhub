from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = '请先登录'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    login_manager.init_app(app)
    
    from app.routes import auth, room
    app.register_blueprint(auth.bp)
    app.register_blueprint(room.bp)
    
    from app.models.user import User
    
    @login_manager.user_loader
    def load_user(pubkey):
        return User.get_by_pubkey(pubkey)
    
    with app.app_context():
        db.create_all()
    
    return app
