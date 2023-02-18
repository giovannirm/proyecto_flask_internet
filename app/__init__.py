from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from app.config import Config


def create_app(): #funcion de fabrica
    app=Flask(__name__)
    app.config.from_object(Config)

    SQLAlchemy(app)
    Marshmallow(app)

    return app
