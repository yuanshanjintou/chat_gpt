# -*- coding:utf-8 -*-
import time
# from datetime import datetime
# from threading import Thread
#
# import openai
#
# from app import app
# from models.keliu import Record
# from utils.mysql_conn import db


class BaseLogic:

    def process_timestamp(self, start_time, end_time, times):

        time_list = [start_time, end_time, times]
        for index, value in enumerate(time_list):
            cur_time = float(value)
            cur_time = time.localtime(cur_time)
            cur_time = time.strftime("%Y-%m-%d %H:%M:%S", cur_time)
            time_list[index] = cur_time

        return time_list

    # def save_message(self, param, group_id, user_id):
    #     # 线程获取数据
    #     thread = Thread(target=self.process_message, args=(param, group_id, user_id))
    #     thread.start()
    #
    # def process_message(self, param, group_id, user_id):
    #     result = ''
    #     completions = openai.ChatCompletion.create(**param, stream=True)  # 分段获取数据
    #     for i, text in enumerate(completions, start=1):
    #         try:
    #             result += text.choices[0]['delta']['content']
    #         except:
    #             continue
    #     print(result)
    #     # 保存回答
    #     current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #     system_dict = {
    #         'group_id': group_id,
    #         'role': 'system',
    #         'record': result,
    #         'create_user_id': user_id,
    #         'create_time': current_time
    #     }
    #     with app.app_context():
    #         record_obj = Record(**system_dict)
    #         db.session.add(record_obj)
    #         db.session.commit()
    #
    #     return result

