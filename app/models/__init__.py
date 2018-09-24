# -*- coding: utf-8 -*-
"""
Created on Apr 7, 2018

@author: guxiwen
"""
from article import Article
from account import User


def fill_with_users(items):
    ids = set(map(lambda a: a.user_id, items))
    users = User.query.filter(User.id.in_(ids))
    users_dic = {}
    for user in users:
        users_dic[user.id] = user
    print users_dic
    result = map(lambda a: _attach_user(a, users_dic[a.user_id]), items)
    return result

def _attach_user(item, user):
    if not user:
        item.user = None
    else:
        item.user = user
    return item