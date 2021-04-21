#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright 2021 Anoyer All Rights Reserved.
# Author: zhihuangliu@foxmail.com
#

from echarts.tools import toolbox


MAX_POINT = {"type": "max", "name": '最大值'}
MIN_POINT = {"type": "min", "name": '最小值'}
AVERAGE_LINE = {"type": "average", "name": '平均值'}


def get_series_bar_data(data=None, name=None, max_point=False, min_point=False,
                        average_line=False, stack=None):
    series_data = {
        "name": name,
        "type": "bar",
        "data": data,
        "markPoint": {
            "data": []
        },
        "markLine": {
            "data": []
        },
        "backgroundStyle": {
            "color": 'rgba(180, 180, 180, 0.2)'
        }
    }
    if max_point is True:
        series_data["markPoint"]["data"].append(MAX_POINT)
    if min_point is True:
        series_data["markPoint"]["data"].append(MIN_POINT)
    if average_line is True:
        series_data["markLine"]["data"].append(AVERAGE_LINE)

    return series_data

