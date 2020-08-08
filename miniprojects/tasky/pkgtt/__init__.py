from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
# local imports
from config import app_config
from flask_migrate import Migrate

db = SQLAlchemy()
app = Flask(__name__, instance_relative_config=False)


def create_app(config_name):
    app.config['FLASK_ENV'] = 'development'
    app.config['FLASK_APP'] = 'runner.py'
    app.config.from_object(app_config['development'])
    app.config.from_object('config.Config')
    db.init_app(app)
    app.config['SECRET_KEY'] = 'randomsecret'
    migrate = Migrate(app, db)
    from pkgtt.models import Blearn
    from pkgtt import routes
    return app
