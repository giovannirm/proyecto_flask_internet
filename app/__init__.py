from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from app.config import Config

# Import db, ma, migrate
from db import db, ma, migrate

from app.routes import *

def create_app(): # Función de fábrica
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    # Blueprints
    app.register_blueprint(company, url_prefix='/companies')
    app.register_blueprint(deparment, url_prefix='/deparments')
    app.register_blueprint(internet_detail, url_prefix='/internet_details')
    app.register_blueprint(establishment, url_prefix='/establishments')
    app.register_blueprint(technology, url_prefix='/technologies')

    return app

