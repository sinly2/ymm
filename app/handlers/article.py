# -*- coding: utf-8 -*-
"""
Created on Aug 23, 2018

@author: guxiwen
"""
from flask import Blueprint, render_template
from ..models.article import Article
from ..models import fill_with_users

__all__ = ['bp']

bp = Blueprint('article', __name__)


@bp.route('/article/<int:article_id>')
def article(article_id=1):
    article = Article.query.filter(Article.id == article_id)


@bp.route('/')
@bp.route('/page/<int:page_id>')
def index(page_id=1):
    article_list = Article.query.get_article_list(page=page_id, page_size=10)
    article_list = fill_with_users(article_list)
    return render_template("index.html", articles=article_list)
