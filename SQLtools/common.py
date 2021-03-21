#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright 2021 Anoyer All Rights Reserved.
# Author: zhihuangliu@foxmail.com
#
__all__ = [
    "get_option"
]

from SQLtools import mysql
from utils import table_global_setting


def get_option(table_uid):
    table_dict = table_global_setting.get_value(table_uid)
    sql_table = mysql.select(table_dict["sql"])
    # TODO: 根据table_dict["type"] 去调用echarts中模块函数，格式化得到option
    option = {}
    return option



