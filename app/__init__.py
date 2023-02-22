from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from app.config import Config
from db import db, migrate, moment

def create_app(): #funcion de fabrica
    app = Flask(__name__)
    app.config.from_object(Config)

    Bootstrap(app)
    SQLAlchemy(app)
    db.init_app(app)
    migrate.init_app(app, db)
    # moment.init_app(app)

    return app