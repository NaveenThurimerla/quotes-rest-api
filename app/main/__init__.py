from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from .config import config_env

db = SQLAlchemy()
flask_bcrypt = Bcrypt()


def create_app(run_env):
    app = Flask(__name__)
    app.config.from_object(config_env[run_env])
    db.init_app(app)
    flask_bcrypt.init_app(app)

    return app
