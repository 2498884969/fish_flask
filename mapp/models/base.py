from contextlib import contextmanager
from datetime import datetime

from flask_sqlalchemy import BaseQuery, SQLAlchemy as _SQLAlchemy
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


class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if 'status' not in kwargs:
            kwargs['status'] = 1
        return super().filter_by(**kwargs)


db = SQLAlchemy(query_class=Query)


class Base(db.Model):
    __abstract__ = True
    create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    def set_attrs(self, attrs_dict: 'dict'):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)

    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return 0
