from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from backend.db import db



def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.config.from_pyfile("../config.py")


    db.init_app(app)

    return app

    
    
    