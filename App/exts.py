# -*- coding=utf-8 -*-
# @Time   :2021/1/7 :20:54
# @Auth   :xuwl
# @Email  :296966596@qq.com
# @File   :exts.py
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension


db = SQLAlchemy()
migrate = Migrate()


def init_ext(app):
    db.init_app(app)
    migrate.init_app(app, db)
    DebugToolbarExtension(app)
