from flask import Flask, make_response, jsonify

from mhelper import is_isbn_or_key
from yushu_book import YuShuBook

app = Flask(__name__)


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


if __name__ == '__main__':
    # nginx + uwsgi
    app.run(host='0.0.0.0', debug=True)
