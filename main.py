#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright 2021 Anoyer All Rights Reserved.
# Author: zhihuangliu@foxmail.com
#

import pymysql
import json

from SQLtools import mysql
from utils.common import read_json_from_file
from utils import mysql_global_setting


if __name__ == "__main__":

    mysql_global_setting.load_data()
    mysql.start()

    sql = """
        SELECT * from test
        """
    result = mysql.select(sql)
    print(result)

    mysql.terminate()


