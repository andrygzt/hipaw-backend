from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS

db =  SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["SQALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "SQLALCHEMY_DATABASE_URI")


    from app.models.post import Post
    from app.models.user import User
    from app.models.pet import Pet

    from .pet_routes import pet_bp
    app.register_blueprint(pet_bp)

    from .user_routes import user_bp
    app.register_blueprint(user_bp)

    from .post_routes import post_bp
    app.register_blueprint(post_bp)

    db.init_app(app)
    migrate.init_app(app, db)

    CORS(app)
    return app