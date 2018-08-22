# -*- coding: utf-8 -*-
"""
Created on Aug 21, 2018

@author: guxiwen
"""
from flask_login import UserMixin
from app import db, login_manager
from _base import SessionMixin

__all__ = ['User']


class User(db.Model, UserMixin, SessionMixin):
    __table__name__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=False)
    password = db.Column(db.String(200))
    nickname = db.Column(db.String(200))
    role = db.Column(db.Integer)
    email = db.Column(db.String(200))
    phone = db.Column(db.String(20))
    status = db.Column(db.Integer)
    create_time = db.Column(db.DateTime)

    def get_id(self):
        return unicode(self.id)

    def verify_password(self, password):
        return password == self.password


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
