# -*- coding: utf-8 -*-
"""
Created on Aug 20, 2018

@author: guxiwen
"""
import sys
sys.path.append('/root/project/TestRequests')
from app import create_app
app = create_app()
if __name__ == '__main__':
    app.run(debug=True,port=50000)