# ./database.py
import os


class Database(object):
    ENV = os.environ['ENV']
    CSRF_ENABLED = True
    SECRET_KEY = "this_is_a_secret_key"
    # Database Configuration
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Database):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + os.environ['DB_USERNAME'] + ':' + os.environ['DB_PASSWORD'] +
    # '@' + \ os.environ['DB_HOST'] + ":33060/" + os.environ['DB_DATABASE']
    SQLALCHEMY_DATABASE_URI = 'postgres://' + os.environ['DB_USERNAME'] + ':' + os.environ['DB_PASSWORD'] + '@' + \
                               os.environ['DB_HOST'] + ':5432/' + os.environ['DB_DATABASE']


class ProductionConfig(Database):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgres://' + os.environ['DB_USERNAME'] + ':' + os.environ['DB_PASSWORD'] + '@' + \
                               os.environ['DB_HOST'] + ':5432/' + os.environ['DB_DATABASE']
