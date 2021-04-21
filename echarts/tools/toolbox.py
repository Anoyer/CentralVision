#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright 2021 Anoyer All Rights Reserved.
# Author: zhihuangliu@foxmail.com
#
__all__ = [
    "tool_box"
]

from utils.common import keyword_to_py


def tool_box(tools_list):
    tools_dict = {}
    for tool in tools_list:
        tools_dict[key] = eval(keyword_to_py(tool) + '()')
    return tools_dict


def data_zoom():
    return {
        "yAxisIndex": "none"
    }


def data_view():
    return {
        "readOnly": False
    }


# 后期考虑加入类型
def magic_type():
    return {
        "type": ["line", "bar"]
    }


def restore():
    return {}


def save_as_image():
    return {}


# {
#         "dataZoom": {
#             "yAxisIndex": "none"
#         },
#         "dataView": {
#             "readOnly": False
#         },
#         "magicType": {
#             "type": ["line", "bar"]
#         },
#         "restore": {},
#         "saveAsImage": {}
# }

