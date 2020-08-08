# Flask config variables
from os import environ, path

project_root = path.abspath(path.dirname(__file__))
basedir = path.dirname(project_root)


class Config(object):
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')


class DevelopmentConfig(Config):
    # Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(basedir, 'tasky\\tasky.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_ECHO = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
# SQLALCHEMY_DATABASE_URI = 'mysql://badri:password''@daily-learning.ctjanlzgevpi.ap-south-1.rds.amazonaws.com:3306/daily_learning'
