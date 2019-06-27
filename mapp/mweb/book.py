"""
 Created by 七月 on 2018-2-1.
"""
from flask import request, render_template, flash

from mapp.libs.mhelper import is_isbn_or_key
from mapp.mforms.book import SearchForm
from mapp.models.gift import Gift
from mapp.models.wish import Wish
from mapp.spider.yushu_book import YuShuBook
from mapp.view_models.book import BookCollection, BookModelView
from mapp.view_models.trade import TradeInfo
from . import web
from flask_login import current_user

__author__ = '七月'


@web.route('/book/search')
def search():
    """
        q :普通关键字 isbn
        page
        ?q=金庸&page=1
    """

    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
    else:
        flash('搜索的关键字不符合要求，请重新输入关键字')
    return render_template('search_result.html', books=books)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    has_in_gifts = False
    has_in_wishes = False

    # 获取书籍详情页的数据
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookModelView(book=yushu_book.first)

    if current_user.is_authenticated:
        if Gift.query.filter_by(user_id=current_user, isbn=isbn,
                                launched=False).first():
            has_in_gifts = True
        if Wish.query.filter_by(user_id=current_user, isbn=isbn,
                                launched=False).first():
            has_in_wishes = True

    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()

    trade_gifts_model = TradeInfo(trade_gifts)
    trade_wishes_model = TradeInfo(trade_wishes)

    return render_template('book_detail.html', book=book,
                           wishes=trade_wishes_model, gifts=trade_gifts_model,
                           has_in_gifts=has_in_gifts, has_in_wishes=has_in_wishes)


