import os

base_dir = os.path.dirname(os.path.abspath(__file__))


class Config():
    DEBUG = False
    DEVELOPMENT = False
    TESTING = False
    SECCRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
    DEBUG = False


class DevConfig(Config):
    DEBUG = True
    DEVELOPMENT = True

class TestConfig(Config):
    TESTING = True