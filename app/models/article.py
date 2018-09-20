# -*- coding: utf-8 -*-
"""
Created on Sep 20, 2018

@author: guxiwen
"""
from app import db
from _base import SessionMixin, get_page
from flask_sqlalchemy import BaseQuery

__all__ = ['Article']


class ArticleQuery(BaseQuery):
    @get_page
    def get_article_list(self, page=1, page_size=10):
        return self.order_by(Article.create_time.desc())


class Article(db.Model, SessionMixin):
    __table__name__ = 'article'
    query_class = ArticleQuery
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    title = db.Column(db.String(200))
    content = db.Column(db.String(200))
    status = db.Column(db.Integer)
    category_id = db.Column(db.Integer)
    tag_id_list = db.Column(db.String(200))
    reader_nums = db.Column(db.Integer)
    create_time = db.Column(db.DateTime)