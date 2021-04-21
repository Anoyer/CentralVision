#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright 2021 Anoyer All Rights Reserved.
# Author: zhihuangliu@foxmail.com
#

# [
#     {"value": 1048, "name": '搜索引擎'},
#     {"value": 735, "name": '直接访问'}
# ]
# TODO: 需要数据格式化
def get_series_pie_data(data=None, name=None):
    series_data = {
        "name": name,
        "type": 'pie',
        "radius": '50%',
        "selectedMode": 'single',
        "selectedOffset": 30,
        "data": data,
        "emphasis": {
            "itemStyle": {
                'shadowBlur': 10,
                "shadowOffsetX": 0,
                "shadowColor": 'rgba(0, 0, 0, 0.5)'
            }
        }
    }

    return series_data

