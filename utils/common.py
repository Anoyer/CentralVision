#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright 2021 Anoyer All Rights Reserved.
# Author: zhihuangliu@foxmail.com
#

__all__ = [
    "read_json_value_from_file",
    "read_json_from_file",
    "write_json_to_file",
    "keyword_to_py"
]


import os
import json


def read_json_value_from_file(key, path_of_file):
    if not os.path.exists(path_of_file):
        return None
    try:
        with open(path_of_file, 'r') as f:
            file_as_dict = json.load(f)
            if key in file_as_dict:
                return file_as_dict[key]
            else:
                return None
    except IOError:
        return None


def read_json_from_file(path_of_file):
    if not os.path.exists(path_of_file):
        return {}

    try:
        with open(path_of_file, 'r') as f:
            return json.load(f)
    except json.decoder.JSONDecodeError as jde:
        print("ReadJsonFromFile: ", jde)

        return {}
    except IOError as ioe:
        print("ReadJsonFromFile: ", ioe)

        return {}


def write_json_to_file(path_of_file, dict_):
    with open(path_of_file, 'w') as file:
        json.dump(
            dict_,
            file,
            sort_keys=True,
            ensure_ascii=False,
            indent=4,
            separators=(
                ',',
                ': '))


# echarts等关键字段变为py风格命名
def keyword_to_py(keyword):
    py_word = ""
    for ch in keyword:
        if 'A' <= ch <= 'Z':
            py_word += f"_{chr(ord(ch) + 32)}"
        elif ch == ' ':
            py_word += '_'
        else:
            py_word += ch
    return py_word

