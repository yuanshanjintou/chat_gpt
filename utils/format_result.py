# -*- coding:utf-8 -*-
from time import time

from flask import jsonify
from objtyping import to_primitive


def format_data(data, rc=0, msg=""):
    data = to_primitive(data)
    if isinstance(data, list):
        data = {
            "data": data
        }
    if not data:
        data = {}
    result = {
        "data": data,
        "status": rc,
        "msg": msg,
        "server_time": int(time())
    }
    return jsonify(result)