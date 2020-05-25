import os

# get the base dir for config file
basedir = os.path.abspath(os.path.dirname(__file__))

# Secret Key Configuration


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "thisIsNewSecretKey")
    DEBUG = False

# Class for Production Env


class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'eProdQuotes.db')


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(basedir, 'eDevQuotes.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'eTestQuotes.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config_env = dict(
    dev=DevConfig,
    test=TestConfig,
    prod=ProdConfig
)


key = Config.SECRET_KEY
