from apscheduler.triggers.interval import IntervalTrigger

from create_app import create_app
from config.config import Config


app, db = create_app(Config)


# @app.before_request
# def login_verify():
#     cookie_dict = request.cookies.to_dict()
#     user_id = cookie_dict.get('token')
#     if not user_id:
#         return Response('123445')


