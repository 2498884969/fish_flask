from flask import Flask
from flask_login.login_manager import LoginManager
from flask_mail import Mail

from mapp.models.base import db

login_manager = LoginManager()
mail = Mail()


def create_app():
    app = Flask(__name__)
    app.config.from_object('mapp.secure')
    app.config.from_object('mapp.settings')

    login_manager.init_app(app=app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先注册或者登陆'

    mail.init_app(app)

    register_blueprint(app)
    register_database(app)
    return app


def register_blueprint(app: 'Flask'):
    from mapp.mweb.book import web
    app.register_blueprint(web)


def register_database(app):
    from mapp.models import book, gift, wish, user

    db.init_app(app=app)
    db.create_all(app=app)
