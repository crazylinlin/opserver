# -*- coding=utf-8 -*-
# @Time   :2021/1/11 :23:29
# @Auth   :xuwl
# @Email  :296966596@qq.com
# @File   :api.py
from flask_restful import Api

from App.api.first import HelloWorld

api = Api()


def init_api(app):
    api.init_app(app)


api.add_resource(HelloWorld, '/hello/')

