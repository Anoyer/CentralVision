#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright 2021 Anoyer All Rights Reserved.
# Author: zhihuangliu@foxmail.com
#

from utils.common import read_json_from_file
import pymysql
import json


if __name__ == "__main__":

    config_dict = read_json_from_file("CentralVision.conf")

    db = pymysql.connect(host=config_dict['host'], user=config_dict['user'], password=config_dict['password'],
                         database=config_dict['database'], charset=config_dict['charset'])
    cursor = db.cursor()

    sql = """
        SELECT * from test
        """
    res = cursor.execute(sql)
    result = cursor.fetchall()
    print(list(zip(*cursor.description))[0])
    print(result)

    cursor.close()

    db.close()


