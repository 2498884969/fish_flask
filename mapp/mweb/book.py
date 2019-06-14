from flask import jsonify

from fisher import app
from mhelper import is_isbn_or_key
from yushu_book import YuShuBook


@app.route('/book/search/<q>/<page>')
def search(q: 'str', page):
    """
    q: 普通关键字
    page:
    """
    isbn_or_key = is_isbn_or_key(q)
    if 'isbn' == isbn_or_key:
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)

    return jsonify(result)
