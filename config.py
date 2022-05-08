import os
# from distutils.command.config import confSQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://username:password@localhost/watchlist'
class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:hotspurs@localhost/pitches'
    SQLALCHEMY_TRACK_MODIFICATIONS = True



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:hotspurs@localhost/pitches'
    DEBUG = True

config_options={
    'development':DevConfig,
    'production':ProdConfig
}