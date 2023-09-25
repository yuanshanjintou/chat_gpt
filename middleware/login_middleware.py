# -*- coding:utf-8 -*-

from flask import request, make_response


def login_verify():
    cookie_dict = request.cookies.to_dict()
    user_id = cookie_dict.get('token')
    if not user_id:
        data = {
            'data': {},
            'status': -1,
            'msg': '请先登录！！'
        }
        response = make_response(data)
        return response
