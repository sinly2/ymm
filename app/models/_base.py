# -*- coding: utf-8 -*-
"""
Created on Aug 22, 2018

@author: guxiwen
"""
from app import db
from flask_sqlalchemy import BaseQuery
import datetime

__all__ = ['SessionMixin', 'get_first_data', 'get_page']


class SessionMixin(object):
    def to_dict(self, *columns):
        dic = {}
        print self.__dict__
        for col in columns:
            value = getattr(self, col)
            dic[col] = value
        return dic

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def self_to_dict(self):
        dic = {}
        for item in self.__dict__:
            if item == "_sa_instance_state":
                continue
            value = getattr(self, item)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%Y-%m-%d %H:%M:%S')
            dic[item] = value
        return dic


class YmmQuery(BaseQuery):
    def filter_in(self, model, values):
        values = set(values)
        if len(values) == 0:
            return {}
        if len(values) == 1:
            ident = values.pop()
            rv = self.get(ident)
            if not rv:
                return {}
            return {ident: rv}
        items = self.filter(model.in_(values))
        dct = {}
        for item in items:
            dct[getattr(item, model.key)] = item
        return dct
#db.Model.query_class = YmmQuery


def get_first_data(func):
    def wrapper(*args, **kwargs):
        item = func(*args, **kwargs)
        if item is None:
            return item
        else:
            return item.first()
    return wrapper


def get_page(func):
    def wrapper(*args, **kwargs):
        item = func(*args, **kwargs)
        if item is None:
            return item
        else:
            return item.limit(kwargs["page_size"]).offset((kwargs["page"]-1)*kwargs["page_size"])
    return wrapper
