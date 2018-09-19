# -*- coding: utf-8 -*-
"""
Created on Apr 7, 2018

@author: guxiwen
"""

def get_first_data(func):
    def wrapper(*args, **kwargs):
        item = func(*args, **kwargs)
        if item is None:
            return item
        else:
            return item.first()
    return wrapper