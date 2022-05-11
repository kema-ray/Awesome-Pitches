import os

# from instance.config import SECRET_KEY
# from distutils.command.config import confSQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://username:password@localhost/watchlist'
class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:hotspurs@localhost/pitches'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    UPLOADED_PHOTOS_DEST ='app/static/photos'



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