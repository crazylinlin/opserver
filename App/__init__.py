# -*- coding=utf-8 -*-
# @Time   :2021/1/7 :18:54
# @Auth   :xuwl
# @Email  :296966596@qq.com
# @File   :__init__.py.py
from flask import Flask

from App.configs import envs
from App.exts import init_ext
from App.api import init_api


def create_app(env):
    app = Flask(__name__)
    app.config.from_object(envs.get(env))
    init_api(app)
    init_ext(app)
    return app
