#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright 2021 Anoyer All Rights Reserved.
# Author: zhihuangliu@foxmail.com
#

import pymysql
import json
from flask import Flask, jsonify

from SQLtools import mysql
from SQLtools.common import get_option
from utils.common import read_json_from_file
from utils import mysql_global_setting, table_global_setting

app = Flask(__name__)
app.config.from_pyfile('config/flask_config.ini')


@app.route('/hello/<usr_id>')
def hello(usr_id: int):
    sql = """
        SELECT * from test
        """
    result = mysql.select(sql)
    return f"{usr_id} {result}"


@app.route('/table-config/')
def get_table_config():
    config_table_list = table_global_setting.get_all_table_config()
    config_table_api_dict = []
    for pos, table in enumerate(config_table_list):
        table_dict = {"uid": pos, "name": table["name"], "api": table["api"], "options": table["options"]}
        config_table_api_dict.append(table_dict)
    return jsonify(config_table_api_dict)


@app.route('/select/<table_uid>')
def get_data(table_uid: int):
    # TODO: 根据table_name 去调用<sql函数>，获取响应的option数据
    option = get_option(table_uid)
    return option


if __name__ == "__main__":
    mysql_global_setting.load_data()
    table_global_setting.load_data()
    mysql.start()

    app.run()
    #
    # sql = """
    #     SELECT * from test
    #     """
    # result = mysql.select(sql)
    # print(result)

    mysql.terminate()


