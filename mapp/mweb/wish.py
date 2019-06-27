from flask import current_app, flash, redirect, url_for
from flask_login import login_required, current_user

from mapp.models.base import db
from mapp.models.wish import Wish
from . import web

__author__ = '七月'


@web.route('/my/wish')
def my_wish():
    pass


@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            gift = Wish()
            gift.isbn = isbn
            gift.uid = current_user.id
            db.session.add(gift)
    else:
        flash('这本书已经加入你的心愿清单或者已经存在于你的赠送清单')
    return redirect(url_for('web.book_detail', isbn=isbn))
    pass


@web.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    pass


@web.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    pass
