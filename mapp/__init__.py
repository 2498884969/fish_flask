from flask import Flask
from flask_login.login_manager import LoginManager

from mapp.models.base import db

login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object('mapp.secure')
    app.config.from_object('mapp.settings')
    db.init_app(app=app)
    db.create_all(app=app)
    login_manager.init_app(app=app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先注册或者登陆'

    register_blueprint(app)
    return app


def register_blueprint(app: 'Flask'):
    from mapp.mweb.book import web
    app.register_blueprint(web)
