# -*- coding: utf-8 -*-
"""
Created on Aug 20, 2018

@author: guxiwen
"""
from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap


db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app():
    app = Flask(__name__)
    #from .main import main as main__blueprint
    #from .auth import auth as auth__blueprint
    #app.config['SECRET_KEY'] = 'hehe'
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://test:test@10.101.94.143:3301/test?charset=utf8'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    #app.register_blueprint(main__blueprint)
    #app.register_blueprint(auth__blueprint,url_prefix='/auth')
    db.init_app(app)
    #bootstrap.init_app(app)
    #login_manager.init_app(app)
    register_routes(app)
    return app


def register_routes(app):
    from .handlers import account
    app.register_blueprint(account.bp)
    return app