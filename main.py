"""app factory"""

from os import getenv

from flask_cors import CORS
from flask_restx import Api
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import config


config_name = getenv('FLASK_ENV', default='production')
api = Api()
db = SQLAlchemy()
migrate = Migrate()


def create_app(config=config[config_name]):
    """Return app object given config object."""
    app = Flask(__name__)
    CORS(app)

    # Lazy initialization with the factory pattern
    api.init_app(app)
    app.config.from_object(config)
    db.init_app(app)
    db.app = app
    migrate.init_app(app, db)

    return app
