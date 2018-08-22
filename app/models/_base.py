# -*- coding: utf-8 -*-
"""
Created on Aug 22, 2018

@author: guxiwen
"""
from app import db

__all__ = ['SessionMixin']


class SessionMixin(object):
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self
