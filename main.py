"""app factory"""

from os import getenv

from flask_cors import CORS
from flask_restx import Api
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import config


config_name = getenv('FLASK_ENV', default='production')
api_prefix = getenv('API_BASE_URL_V1', default='/api/v1')
rest_api = Api(prefix=api_prefix, version='1.0', title='Game API',
               description='Game localization API', doc="/docs")
db = SQLAlchemy()
migrate = Migrate()


def create_app(config=config[config_name]):
    """Return app object given config object."""
    app = Flask(__name__)
    CORS(app)

    # Lazy initialization with the factory pattern
    rest_api.init_app(app)
    app.config.from_object(config)
    db.init_app(app)
    db.app = app
    migrate.init_app(app, db)

    # import models
    import api.models
    # import views
    import api.views

    return app
