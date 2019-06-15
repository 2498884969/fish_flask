from flask import Flask

from mapp.mweb.book import web


def create_app():
    app = Flask(__name__)
    register_blueprint(app)
    return app


def register_blueprint(app: 'Flask'):
    app.register_blueprint(web)
