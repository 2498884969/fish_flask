from flask import Flask

from mapp.mweb.book import web
from mapp.models.book import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('mapp.secure')
    app.config.from_object('mapp.settings')
    db.init_app(app=app)
    db.create_all(app=app)

    register_blueprint(app)
    return app


def register_blueprint(app: 'Flask'):
    app.register_blueprint(web)
