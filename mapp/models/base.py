from contextlib import contextmanager
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from sqlalchemy import Column, SmallInteger, Integer
import logging


class SQLAlchemy(_SQLAlchemy):

    @contextmanager
    def auto_commit(self):
        try:
            yield
            db.session.commit()
        except Exception:
            db.session.rollback()
            logging.error('Faild to get result', exc_info=True)


db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)

    def set_attrs(self, attrs_dict: 'dict'):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())
