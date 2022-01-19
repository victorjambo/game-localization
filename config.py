"""App config"""

from os import getenv


class Config(object):
    """Base Config"""

    SQLALCHEMY_DATABASE_URI = getenv(
        'DATABASE_URI', default='postgresql://localhost/game')
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """Prod Config"""

    pass


class DevelopmentConfig(Config):
    """Dev Config"""

    DEBUG = True


class TestingConfig(Config):
    """Test Config"""

    TESTING = True
    SQLALCHEMY_DATABASE_URI = getenv(
        'TEST_DATABASE_URI', default='postgresql://localhost/game_test')


config = {
    'development': DevelopmentConfig,
    'staging': ProductionConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
