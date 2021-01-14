# -*- coding=utf-8 -*-
# @Time   :2021/1/11 :23:32
# @Auth   :xuwl
# @Email  :296966596@qq.com
# @File   :first.py
from flask_restful import Resource


class HelloWorld(Resource):

    def get(self):
        return {
            'msg': 'hello,world!!!'
        }