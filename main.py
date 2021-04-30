#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright 2021 Anoyer All Rights Reserved.
# Author: zhihuangliu@foxmail.com
#

import pymysql
import json
from flask import Flask, jsonify, make_response

from SQLtools import mysql
from SQLtools.common import get_option
from utils.common import read_json_from_file, keyword_to_py
from utils import mysql_global_setting, table_global_setting

app = Flask(__name__)
app.config.from_pyfile('config/flask_config.ini')


@app.route('/hello/<usr_id>')
def hello(usr_id: int):
    sql = """
        SELECT name,success,age from test
        """
    result = mysql.select(sql)
    return f"{usr_id} {result}"


@app.route('/api/table-config/')
def get_table_config():
    config_table_list = table_global_setting.get_all_table_config()
    config_table_api_dict = {"os_name": config_table_list.get("os_name"), "table_group": {}}
    for pos, table in enumerate(config_table_list.get("table_list")):
        table_dict = {"uid": table.get("uid"), "name": table.get("name")}
        if table.get("group_name") not in config_table_api_dict["table_group"]:
            config_table_api_dict["table_group"][table["group_name"]] = []
        config_table_api_dict["table_group"][table["group_name"]].append(table_dict)
    response = make_response(jsonify(config_table_api_dict))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route('/api/select/<int:table_uid>')
def get_data(table_uid: int):
    # TODO: 根据table_name 去调用<sql函数>，获取响应的option数据
    option = get_option(table_uid)
    response = make_response(jsonify(option))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


if __name__ == "__main__":
    mysql_global_setting.load_data()
    table_global_setting.load_data()
    mysql.start()
    app.run(host='0.0.0.0', debug=True)
    #
    # sql = """
    #     SELECT * from test
    #     """
    # result = mysql.select(sql)
    # print(result)

    mysql.terminate()


