# -*- coding: utf-8 -*-
"""
Created on Aug 20, 2018

@author: guxiwen
"""

from flask import Blueprint, request
from ..models.account import User

__all__ = ['bp']

bp = Blueprint('account', __name__)


@bp.route('/index', methods=['GET'])
def index():
    return 'ok'


@bp.route('/login', methods=['GET'])
def login():
    return 'ok'


@bp.route('/verifyPassword', methods=['POST', 'GET'])
def verify_password():
    username = request.args.get('username')
    password = request.args.get('password')
    user = User.query.filter(User.username == username).first()
    if user.verify_password(password):
        return '222'
    else:
        return '333'
