from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, desc, func
from sqlalchemy.orm import relationship
from flask import current_app

from mapp.spider.yushu_book import YuShuBook
from .base import Base, db


class Gift(Base):
    __tablename__ = 'gift'

    id = Column(Integer, primary_key=True)
    uid = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')
    isbn = Column(String(13))
    launched = Column(Boolean, default=False)

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(isbn=self.isbn)
        return yushu_book.first

    @classmethod
    def recent(cls):
        return Gift.query.filter_by(launched=False).group_by(Gift.isbn).order_by(desc(Gift.create_time)).limit(
            current_app.config['RECENT_BOOK_COUNT']).distinct().all()

    @classmethod
    def get_user_gifts(cls, uid):
        gifts = Gift.query.filter_by(launched=False, uid=uid).order_by(desc(Gift.create_time)).all()
        return gifts

    @classmethod
    def get_wish_counts(cls, isbn_list):
        from mapp.models.wish import Wish

        count_list = db.session.query(func.count(Wish.id), Wish.isbn).filter(Wish.launched == False, Wish.status == 1,
            Wish.isbn.in_(isbn_list)).group_by(Wish.isbn).all()

        count_list = [dict(count=w[0], isbn=w[1]) for w in count_list]
        return count_list

    def is_yourself_gift(self, uid):
        return True if self.uid == uid else False


