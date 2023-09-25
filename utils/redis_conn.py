# 封装redis连接对象
import redis
from flask import current_app


class Redis(object):

    def __init__(self):
        # 初始化redis连接对象
        self.rds = redis.Redis(
            host=current_app.config.get('REDIS_HOST'),
            port=current_app.config.get('REDIS_PORT'),
            password=current_app.config.get('REDIS_PASSWORD'),
            db=current_app.config.get('REDIS_DB')
        )

    def get_redis_data(self, key):
        data = self.rds.get(key)
        return data

    def set_redis_data(self, key, value, expires_time=None):
        data = value
        self.rds.set(
            name=key,
            value=data,
            ex=expires_time  # 第三个参数表示Redis过期时间,不设置则默认不过期
        )

