import json

from flask import jsonify, request, render_template, flash

from mapp.libs.mhelper import is_isbn_or_key
from mapp.mforms.book import SearchForm
from mapp.spider.yushu_book import YuShuBook
from mapp.view_models.book import BookModelView, BookCollection
from . import web


@web.route('/book/search')
def search():
    """
    q: 普通关键字
    page:
    """
    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if 'isbn' == isbn_or_key:
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
        return json.dumps(yushu_book, default=lambda o: o.__dict__)
        # return jsonify(books)
    else:
        return jsonify(form.errors)


@web.route('/test')
def test():
    data = dict(name='强旭辉', age=19)
    flash('hehe')
    flash('haha')
    return render_template('test.html', data=data)
