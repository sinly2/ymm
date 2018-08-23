# -*- coding: utf-8 -*-
"""
Created on Aug 23, 2018

@author: guxiwen
"""
from flask import Blueprint, request

__all__ = ['bp']

bp = Blueprint('article', __name__)


@bp.route('/article/<int:article_id>')
def article(article_id=1):
    pass
