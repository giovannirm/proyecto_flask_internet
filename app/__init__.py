from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from app.config import Config

# from app.routes import company

migrate = Migrate()
db = SQLAlchemy()
ma = Marshmallow()

def create_app(): # Función de fabrica
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    # Blueprints
    # app.register_blueprint(company)

    return app