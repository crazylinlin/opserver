# -*- coding=utf-8 -*-
# @Time   :2021/1/7 :20:54
# @Auth   :xuwl
# @Email  :296966596@qq.com
# @File   :configs.py
from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent


def get_db_uri(dbinfo):
    dialect = dbinfo.get('DIALECT') or 'sqllite'
    driver = dbinfo.get('DRIVER') or 'sqllite'
    username = dbinfo.get('USERNAME') or ''
    password = dbinfo.get('PASSWORD') or ''
    host = dbinfo.get('HOST') or ''
    port = dbinfo.get('PORT') or ''
    database = dbinfo.get('DATABASE') or ''
    return '{}+{}://{}:{}@{}:{}/{}'.format(dialect, driver, username, password,
                                           host, port, database)


class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    DEBUG = True
    dbinfo = {
        'DIALECT': 'mysql',
        'DRIVER': 'pymysql',
        'USERNAME': 'root',
        'PASSWORD': 'xuwl123654',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'DATABASE': 'db_flask'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class TestConfig(Config):
    DEBUG = False
    dbinfo = {
        'DIALECT': 'mysql',
        'DRIVER': 'pymysql',
        'USERNAME': 'root',
        'PASSWORD': 'xuwl123654',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'DATABASE': 'db_flask'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class ProductConfig(Config):
    DEBUG = False
    dbinfo = {
        'DIALECT': 'mysql',
        'DRIVER': 'pymysql',
        'USERNAME': 'root',
        'PASSWORD': 'xuwl123654',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'DATABASE': 'db_flask'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


envs = {
    'development': DevelopConfig,
    'testing': TestConfig,
    'product': ProductConfig,
    'default': DevelopConfig,
}
