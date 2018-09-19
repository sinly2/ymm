# -*- coding: utf-8 -*-
"""
Created on Aug 23, 2018

@author: guxiwen
"""
from flask import Blueprint, request
from ..models.article import Article

__all__ = ['bp']

bp = Blueprint('article', __name__)


@bp.route('/article/<int:article_id>')
def article(article_id=1):
    article = Article.query.filter(Article.id == article_id)


@bp.route('/')
@bp.route('/page/<int:pageid>')
def index(pageid=1):
    pass
