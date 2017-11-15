# app/__init__.py

# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import  LoginManager

# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()
# initialize the login_manager
login_manager = LoginManager()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
   # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_pyfile('config.py')
    db.init_app(app)
    # pass your app into the login_manager instance
    login_manager.init_app(app)
    """The default message when someone gets redirected to the login page"""
    login_manager.login_message = "You must be logged in to access this page"
    """You also need to tell flask_login where it should redirect someone to if they try to access a private route."""
    login_manager.login_view = "auth.login"


    return app