from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, desc, func
from sqlalchemy.orm import relationship

from mapp.models.base import Base, db
from mapp.spider.yushu_book import YuShuBook


class Wish(Base):
    __tablename__ = 'wish'

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
    def get_user_wishes(cls, uid):
        wishes = Wish.query.filter_by(launched=False, uid=uid).order_by(
            desc(Wish.create_time)).all()
        return wishes

    @classmethod
    def get_gift_counts(cls, isbn_list):
        from mapp.models.gift import Gift
        count_list = db.session.query(func.count(Gift.id), Gift.isbn).filter(
            Gift.launched == False,
            Gift.status == 1,
            Gift.isbn.in_(isbn_list)).group_by(Gift.isbn).all()

        count_list = [dict(count=w[0], isbn=w[1]) for w in count_list]
        return count_list
