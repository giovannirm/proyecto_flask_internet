from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from app.config import Config
from db import db, migrate

def create_app(): # Función de fabrica
    app = Flask(__name__)
    app.config.from_object(Config)

    SQLAlchemy(app)
    Marshmallow(app)

    db.init_app(app)
    migrate.init_app(app, db)

    return app