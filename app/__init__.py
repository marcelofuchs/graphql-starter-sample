# app/__init__.py
from app.config.database import Database
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_graphql import GraphQLView

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # Allows you to get configurations
    # from the config file with the exact environment
    # that you require
    app.config.from_object((get_environment_config()))
    db.init_app(app)

    @app.before_first_request
    def initialize_database():
        """ Create all tables """
        db.create_all()

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.session.remove()

    from app.schema import schema

    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True  # for having the GraphiQL interface
        )
    )

    @app.route("/")
    def hello_world():
        return "Hello World!"

    return app


def get_environment_config():
    if Database.ENV == "PRODUCTION":
        return "app.config.database.ProductionConfig"
    elif Database.ENV == "DEVELOPMENT":
        return "app.config.database.DevelopmentConfig"
