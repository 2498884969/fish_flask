
from flask_login import login_required, current_user
from flask import current_app, flash

from mapp.models.base import db
from . import web
from mapp.models.gift import Gift
__author__ = '七月'


@web.route('/my/gifts')
@login_required
def my_gifts():
    return 'my gifts'
    pass


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
    else:
        flash('这本书已经加入你的心愿清单或者已经存在于你的赠送清单')
    return 'success'


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass



