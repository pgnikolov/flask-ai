from flask import Flask
from config import Config
from .routes import main
from .models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(main)

    return app
