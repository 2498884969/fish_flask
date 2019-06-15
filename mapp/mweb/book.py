from flask import jsonify, request
from flask import Blueprint

from mapp.libs.mhelper import is_isbn_or_key
from mapp.mforms.book import SearchForm
from mapp.spider.yushu_book import YuShuBook
from . import web


@web.route('/book/search')
def search():
    """
    q: 普通关键字
    page:
    """
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if 'isbn' == isbn_or_key:
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)
        return jsonify(result)
    else:
        return jsonify(form.errors)
