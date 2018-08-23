# -*- coding: utf-8 -*-
"""
Created on Aug 20, 2018

@author: guxiwen
"""

from flask import Blueprint, request
from flask_login import login_user, login_required, logout_user
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
    login_user(user=user, remember=False)
    if user.verify_password(password):
        return '222'
    else:
        return '333'


@bp.route('/test', methods=['GET'])
@login_required
def test():
    return "hahaah"


@bp.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return 'You have logged out...'
