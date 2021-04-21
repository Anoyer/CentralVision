#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright 2021 Anoyer All Rights Reserved.
# Author: zhihuangliu@foxmail.com
#

from echarts.tools import toolbox

# TODO：后期将一些常量规整
DEFAULT_X_DATA = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
SERIES_DATA = [{"name": "default", "data": [150, 230, 224, 218, 135, 147, 260], "type": "line", "smooth": False}]


# boundary_gap x坐标是否取左侧
# data_zoom x选择栏
# tool_list 图标工具栏
# TODO：分阶段颜色设置 https://echarts.apache.org/examples/zh/editor.html?c=line-aqi
# TODO: 多x轴 https://echarts.apache.org/examples/zh/editor.html?c=multiple-x-axis
# TODO：雨量关系图 https://echarts.apache.org/examples/zh/editor.html?c=area-rain-fall
# TODO: 考虑添加动态数据 https://echarts.apache.org/examples/zh/editor.html?c=dynamic-data2
# TODO: 考虑添加动态多折线数据 https://echarts.apache.org/examples/zh/editor.html?c=line-race
# TODO：将其整合line、bar、pie、k、radar、funnel  考虑整合：sunburst、tree、SCORE
# TODO: 支持x，y轴多元化
def get_option(title="", x_data=None, series_data_list=None, tool_list=None,
                           legend_flag=False, boundary_gap=False, data_zoom=False):
    if tool_list is None:
        tool_list = []
    if series_data_list is None:
        series_data_list = SERIES_DATA
    if x_data is None:
        x_data = DEFAULT_X_DATA
    tool_box_feature = toolbox.tool_box(tool_list)
    option = {
        "title": {
           "text": title
        },
        "tooltip": {
            "trigger": "axis"
        },
        "toolbox": {
            "show": True,
            "feature": tool_box_feature
        },
        "xAxis": [{
          "type": "category",
          "boundaryGap": boundary_gap,
          "data": x_data
        }],
        "yAxis": [{
          "type": "value"
        }],
        "dataZoom": [{
            "type": 'inside'
        }],
        "series": series_data_list
    }
    # 设置标题
    if title is None:
        option["title"] = {"text": title}
    # 设置legend
    if legend_flag is True:
        legend = []
        for data in series_data_list:
            legend.append(data["name"])
        option["legend"] = legend
    # 设置x轴滑动条
    if data_zoom is True:
        option["dataZoom"].append({})
    return option


