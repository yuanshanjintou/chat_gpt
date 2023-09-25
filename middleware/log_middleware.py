# 模拟中间件
class Md(object):
    def __init__(self, old_wsgi_app):
        self.old_wsgi_app = old_wsgi_app

    def __call__(self, environ, start_response):
        print(environ.get('werkzeug.request').__dict__)
        ret = self.old_wsgi_app(environ, start_response)
        print('结束之后')
        return ret
