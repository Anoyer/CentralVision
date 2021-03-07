#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright 2021 Anoyer All Rights Reserved.
# Author: zhihuangliu@foxmail.com
#

import pymysql
import json
from flask import Flask

from SQLtools import mysql
from utils.common import read_json_from_file
from utils import mysql_global_setting

app = Flask(__name__)


@app.route('/hello/<usr_id>')
def hello(usr_id):
    sql = """
        SELECT * from test
        """
    result = mysql.select(sql)
    return f"{usr_id} {result}"


if __name__ == "__main__":
    mysql_global_setting.load_data()
    mysql.start()
    app.run()
    #
    # sql = """
    #     SELECT * from test
    #     """
    # result = mysql.select(sql)
    # print(result)

    mysql.terminate()


