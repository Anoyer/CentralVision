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


# smooth 线段是否平滑
# area_style 是否为面积图
# TODO: area_style 格式化支持，stack支持
def get_series_line_data(data=None, name=None, smooth=False, max_point=False, min_point=False,
                         average_line=False, area_style=None, stack=None):
    series_data = {
        "name": name,
        "type": "line",
        "data": data,
        "smooth": smooth,
        "markPoint": {
            "data": []
        },
        "markLine": {
            "data": []
        }
    }
    if area_style is not None:
        series_data["areaStyle"] = area_style
    if max_point is True:
        series_data["markPoint"]["data"].append(MAX_POINT)
    if min_point is True:
        series_data["markPoint"]["data"].append(MIN_POINT)
    if average_line is True:
        series_data["markLine"]["data"].append(AVERAGE_LINE)

    return series_data

