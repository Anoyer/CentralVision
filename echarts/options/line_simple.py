#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright 2021 Anoyer All Rights Reserved.
# Author: zhihuangliu@foxmail.com
#

DEFAULT_X_DATA = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
SERIES_DATA = [{"name": "default", "data": [150, 230, 224, 218, 135, 147, 260], "type": "line", "smooth": False}]
MAX_POINT = {"type": "max", "name": '最大值'}
MIN_POINT = {"type": "min", "name": '最小值'}
AVERAGE_LINE = {"type": "average", "name": '平均值'}


# boundary_gap x坐标是否取左侧
# TODO：考虑是否tooltip 通过字段可设置
# TODO：legend 添加
# TODO：分阶段颜色设置 https://echarts.apache.org/examples/zh/editor.html?c=line-aqi
# TODO: 多x轴 https://echarts.apache.org/examples/zh/editor.html?c=multiple-x-axis
# TODO：雨量关系图 https://echarts.apache.org/examples/zh/editor.html?c=area-rainfall
# TODO: 考虑添加动态数据 https://echarts.apache.org/examples/zh/editor.html?c=dynamic-data2
# TODO: 考虑添加动态多折线数据 https://echarts.apache.org/examples/zh/editor.html?c=line-race

def get_line_simple_option(title="", x_data=None, series_data_list=None, boundary_gap=False):
    if series_data_list is None:
        series_data_list = SERIES_DATA
    if x_data is None:
        x_data = DEFAULT_X_DATA
    option = {
       "title": {
           "text": title
       },
        "tooltip": {
            "trigger": "axis"
        },
        "toolbox": {
            "show": True,
            "feature": {
                "dataZoom": {
                    "yAxisIndex": "none"
                },
                "dataView": {
                    "readOnly": False
                },
                "magicType": {
                    "type": ["line", "bar"]
                },
                "restore": {},
                "saveAsImage": {}
            }
        },
        "xAxis": {
          "type": "category",
          "boundaryGap": boundary_gap,
          "data": x_data
       },
       "yAxis": {
          "type": "value"
       },
       "series": series_data_list
    }
    if title is None:
        option["title"] = {"text": title}
    return option


# smooth 线段是否平滑
# area_style 是否为面积图
# TODO: area_style 格式化支持，stack支持
def get_series_data(data=None, name=None, smooth=False, max_point=False, min_point=False,
                    area_style=None, average_line=False, stack=None):
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


