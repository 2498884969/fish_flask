from sqlalchemy import Column, Integer, String, Boolean, Float
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app

from mapp.libs.mhelper import is_isbn_or_key
from mapp.models.gift import Gift
from mapp.models.wish import Wish
from mapp.spider.yushu_book import YuShuBook
from .base import Base, db
from mapp import login_manager


class User(UserMixin, Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    _password = Column('password', String(100))

    def generate_token(self, expiration=600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps(dict(id=self.id)).decode('utf-8')

    @staticmethod
    def reset_password(token, new_password):

        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except Exception:
            return False

        uid = data['id']
        with db.auto_commit():
            user = User.query.get(uid)
            user.password = new_password
        return True

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, item):
        self._password = generate_password_hash(item)

    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    def can_save_to_list(self, isbn):
        if is_isbn_or_key(isbn) != 'isbn':
            return False
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(isbn)
        if yushu_book.first is None:
            return False
        # 不允许同一个用户同时赠送多本相同的书
        # 不允许一本书存在于心愿清单的同时存在于赠送清单
        gifting = Gift.query.filter_by(uid=self.id, isbn=isbn,
                                       launched=False).first()
        wishing = Wish.query.filter_by(uid=self.id, isbn=isbn,
                                       launched=False).first()
        if not gifting and not wishing:
            return True
        else:
            return False


@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))