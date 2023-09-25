from utils.log_setting import after_request
from views.base import MessageLogic, Login, SaveMessage


# 注册路由
def register_url(app):
    # 基础数据接口路由

    app.add_url_rule(rule='/api/gpt', view_func=MessageLogic.as_view('gpt'))
    app.add_url_rule(rule='/api/login', view_func=Login.as_view('login'))
    app.add_url_rule(rule='/api/save_message', view_func=SaveMessage.as_view('save_message'))
    # app.after_request(after_request)
    return app
