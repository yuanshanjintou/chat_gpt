import datetime
import os
import traceback
from functools import wraps
from flask import request

from settings import LOG_DIR


def err_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            with open(LOG_DIR, 'a') as f:
                f.write(traceback.format_exc())
            raise

    return wrapper


def after_request(response):
    path = request.path
    method = request.method
    if path == '/api/gpt' and method == "GET":
        data = response.data.decode('utf-8')
        print(data)
    return response
