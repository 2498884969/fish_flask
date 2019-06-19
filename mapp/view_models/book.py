class BookModelView:

    def __init__(self, book):
        self.title = book['title']
        self.author = '、'.join(book['author'])
        self.publisher = book['publisher']
        self.image = book['images']['large']
        self.price = book['price']
        self.summary = book['summary']
        self.pages = book['pages']


class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookModelView(book) for book in yushu_book.books]


class _BookModelView:

    @classmethod
    def package_single(cls, data, keyword):
        ret = dict(books=[], total=0, keyword=keyword)
        if data:
            ret['total'] = 1
            ret['books'] = [cls.__cut_book_data(data)]
        return ret

    @classmethod
    def package_collections(cls, data, keyword):
        ret = dict(books=[], total=0, keyword=keyword)
        if data:
            ret['total'] = len(data['books'])
            ret['books'] = [cls.__cut_book_data(book) for book in data['books']]
        return ret

    @classmethod
    def __cut_book_data(cls, data):
        book = {'title': data['title'], 'author': '、'.join(data['author']), 'publisher': data['publisher'],
                'image': data['images'], 'price': data['price'], 'summary': data['summary'] or '',
                'pages': data['pages'] or ''}
        return book
