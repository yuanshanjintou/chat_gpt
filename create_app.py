import logging

from flask import Flask
from flask_migrate import Migrate
from werkzeug.exceptions import HTTPException
from flask_cors import CORS

from settings import LOG_DIR
from logging.handlers import TimedRotatingFileHandler
from middleware.login_middleware import login_verify
from apscheduler.schedulers.background import BackgroundScheduler

from urls.archive import register_url
from utils.mysql_conn import db


def handle_param_exception(e):
    print('异常捕捉')
    response = e.get_response()
    return response


class RequestParamException(HTTPException):
    code = 500


migrate = Migrate()


def create_app(config):
    # 初始化flask实例对象
    archive_app = Flask(__name__)
    archive_app.config.from_object(config)

    # 日志
    logger = logging.getLogger('werkzeug')
    handler = TimedRotatingFileHandler(filename=LOG_DIR, when='midnight', backupCount=7, encoding='utf-8')
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    # 跨域
    CORS(archive_app)

    archive_app.register_error_handler(RequestParamException, handle_param_exception)
    # 注册登录权限验证
    # archive_app.before_request(login_verify)
    # 注册路由
    archive_app = register_url(archive_app)
    # 数据库连接初始化
    db.init_app(archive_app)
    # migrate.init_app(app=archive_app, db=db)

    return archive_app, db
