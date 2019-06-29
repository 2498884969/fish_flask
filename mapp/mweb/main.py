from flask import render_template

from mapp.models.gift import Gift
from mapp.view_models.book import BookModelView
from . import web


__author__ = '七月'


@web.route('/')
def index():
    recent_gifts = Gift.recent()
    books = [BookModelView(gift.book) for gift in recent_gifts]
    return render_template('index.html', recent=books)


@web.route('/personal')
def personal_center():
    pass
