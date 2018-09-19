# -*- coding: utf-8 -*-
"""
Created on Aug 22, 2018

@author: guxiwen
"""
from app import db
from flask_sqlalchemy import BaseQuery

__all__ = ['SessionMixin']


class SessionMixin(object):
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self


class YmmQuery(BaseQuery):
    def filter_in(self):
        print dir(YmmQuery)
        pass
#db.Model.query_class = YmmQuery

def get_first_data(func):
    def wrapper(*args, **kwargs):
        item = func(*args, **kwargs)
        if item is None:
            return item
        else:
            return item.first()
    return wrapper