# -*- coding:utf-8 -*-
import copy
import itertools
from datetime import datetime

import requests
from flask import request, views, Response, make_response, current_app

from logic.base import BaseLogic
from models.keliu import *
from utils.format_result import format_data
from objtyping import to_primitive
# from app import app
import openai


class Login(views.MethodView):

    def post(self):
        user_name = request.form.get('user_name')
        pass_word = request.form.get('pass_word')

        user_data = User.query.filter(User.account == user_name).first()

        if not user_data:
            data, rc, msg = {}, -1, '用户不存在'
            return format_data(data, rc, msg)

        if user_data.password != pass_word:
            data, rc, msg = {}, -1, '用户密码错误'
            return format_data(data, rc, msg)

        data, rc, msg = {}, 0, ''
        response = make_response(format_data(data, rc, msg))
        response.set_cookie('token', str(user_data.id))
        return response


class GroupLogic(views.MethodView):

    def get(self):
        user_id = request.cookies.get('token')

        group_query_list = Group.query.filter(Group.create_user_id == user_id).order_by(Group.update_time).all()

        group_list = to_primitive(group_query_list)
        return format_data(group_list)

    def post(self):
        user_id = request.cookies.get('token')
        group_name = request.form.get('group_name')

        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        group_dict = {
            "group_name": group_name,
            "create_user_id": user_id,
            "update_user_id": user_id,
            "create_time": current_time,
            "update_time": current_time
        }

        try:
            group_obj = Group(**group_dict)
            db.session.add(group_obj)
            db.session.commit()
            data, rc, msg = {}, 0, ''
            return format_data(data, rc, msg)
        except Exception as e:
            db.session.rollback()
            data, rc, msg = {}, -1, '新增错误'
            return format_data(data, rc, msg)


class MessageLogic(views.MethodView):


    def post(self):
        group_id = request.args.get('group_id')
        page = int(request.args.get('page'))
        page_num = int(request.args.get('page_num'))

        data = Record.query.filter(Record.group_id == group_id).order_by(Record.create_time.desc())
        start_offset = (page - 1) * page_num
        data_query_list = data.offset(start_offset).limit(page_num).all()

        record_list = to_primitive(data_query_list)
        return format_data(record_list)

    def get(self):
        group_id = request.args.get('group_id')
        user_id = request.cookies.get('token', 1)
        question = request.args.get('question')

        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        deep_num = RelationDeep.query.filter(RelationDeep.user_id == user_id).first().deep_num
        record_query_list = Record.query.filter(Record.group_id == group_id).order_by(Record.create_time.desc())
        record_list = record_query_list.limit(deep_num*2).all()

        # 保存问题
        user_dict = {
            'group_id': group_id,
            'role': 'user',
            'record': question,
            'create_user_id': user_id,
            'create_time': current_time
        }

        record_obj = Record(**user_dict)
        db.session.add(record_obj)
        db.session.commit()

        message_list = []
        for record in record_list:
            cur_dict = {
                "role": record.role,
                "content": record.record
            }
            message_list.append(cur_dict)

        question_list = [{"role": "user", "content": question}]
        message_list = message_list[::-1] + question_list

        openai.organization = "org-STXuIOWuuVbYuOdyd5czNhlJ"
        openai.api_key = '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'

        param = {
            'model': "gpt-3.5-turbo",
            'messages': message_list
        }

        completions = openai.ChatCompletion.create(**param, stream=True)  # 分段获取数据
        for ms in message_list:
            print(ms)
        from itertools import tee
        completions1, completions2 = tee(completions)

        def generate():
            for i, text in enumerate(completions1, start=1):
                try:
                    result = text.choices[0]['delta']['content']
                    yield result
                except Exception as e:
                    continue

        headers = {
            'Content-Type': 'text/event-stream',
            'Cache-Control': 'no-cache',
            'X-Accel-Buffering': 'no',
        }
        self.process_message(completions2, group_id, user_id)

        return Response(generate(), mimetype="text/event-stream", headers=headers)

    def process_message(self, completions2, group_id, user_id):
        result = ''
        for i, text in enumerate(completions2, start=1):
            try:
                result += text.choices[0]['delta']['content']
            except:
                continue
        # print(result)
        data = {
            "text": result,
            "group_id": group_id,
            "user_id": user_id
        }
        url = 'http://127.0.0.1:8089/api/save_message'
        requests.post(url, data=data)
        return result


class SaveMessage(views.MethodView):
    def post(self):
        text = request.form.get('text')
        group_id = request.form.get('group_id')
        user_id = request.form.get('user_id')

        # 保存回答
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        system_dict = {
            'group_id': group_id,
            'role': 'system',
            'record': text.replace("'", "\\'"),
            'create_user_id': user_id,
            'create_time': current_time
        }
        print(system_dict)
        record_obj = Record(**system_dict)
        db.session.add(record_obj)
        db.session.commit()
        data, rc, msg = {}, 0, ''
        return format_data(data, rc, msg)



