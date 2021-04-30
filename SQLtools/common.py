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
from echarts import option
from echarts.series import bar, line, funnel, k, line, pie, radar


def get_option(table_uid: int):
    table_dict = table_global_setting.get_value(table_uid)
    sql_table = mysql.select(table_dict["sql"])
    sql_table_list = get_sql_table_list(sql_table)
    # TODO: 根据table_dict["type"] 去调用echarts中模块函数，格式化得到option
    series_list = []
    for series_obj in table_dict.get("series", []):
        # TODO: 考虑函数指针, 将函数封装成字典，传参方便, 思考传参如何传，考虑直接传字典，否则参数太多
        series_list.append(eval(f"{series_obj['type']}.get_series_{series_obj['type']}_data("
                                f"sql_table_list[series_obj['data_name']], "
                                f"series_obj.get('table_name'))"))

    # print(table_dict)
    # print(sql_table_list)
    option_data = option.get_option(table_dict.get('name', ''),
                                    sql_table_list[table_dict['xAxis'][0]['data_name']],
                                    series_list)
    return option_data


# List by index
def get_sql_table_list(sql_table: dict):
    sql_table_list = {}
    for elem in sql_table:
        for key in elem:
            if key not in sql_table_list:
                sql_table_list[key] = []
            sql_table_list[key].append(elem[key])

    return sql_table_list

