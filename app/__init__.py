from flask import Flask
from config import config_options

def create_app(config_name):

    # initializing the application
    app = Flask(__name__)

    # setting up configurations
    app.config.from_object(config_options[config_name])