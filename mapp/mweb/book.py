"""
 Created by 七月 on 2018-2-1.
"""
from flask import jsonify, request, current_app, url_for, render_template, flash
import json

from mapp.libs.mhelper import is_isbn_or_key
from mapp.mforms.book import SearchForm
from mapp.spider.yushu_book import YuShuBook
from mapp.view_models.book import BookCollection, BookModelView
from . import web

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
        # return jsonify(form.errors)
    return render_template('search_result.html', books=books)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookModelView(book=yushu_book.first)
    return render_template('book_detail.html', book=book, wishes=[], gifts=[])


