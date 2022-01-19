import os
import pytest

from config import config
from main import create_app, db
from api.models import Game

from .mock import games_data

config_name = 'testing'
os.environ['FLASK_ENV'] = config_name


@pytest.fixture(scope='session')
def app():
    """Setup our flask test app, this only gets executed once.
    """
    _app = create_app(config[config_name])

    # Establish an application context before running the tests.
    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture(scope='function')
def client(app):
    """Setup an app client, this gets executed for each test function.
    """
    yield app.test_client()


@pytest.fixture(scope='module')
def init_db(app):
    """initialize db
    """
    db.create_all()
    yield db
    db.session.close()
    db.drop_all()


@pytest.fixture(scope="module")
def new_game(app):
    return Game(**games_data[0])
