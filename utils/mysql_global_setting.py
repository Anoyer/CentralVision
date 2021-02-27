#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright 2021 Anoyer All Rights Reserved.
# Author: zhihuangliu@foxmail.com
#
__all__ = [
    "load_data"
]

import pymysql
import os

from utils.common import read_json_from_file

_global_dict = {}


def get_cwd():
    return os.getcwd()


def load_data():
    global _global_dict
    run_path = get_cwd()
    _global_dict = read_json_from_file("MySql.conf")
    _set_value("run_path", run_path)


def _set_value(key, value):
    _global_dict[key] = value


def get_value(key, default_value=None):
    try:
        return _global_dict[key]
    except KeyError:
        return default_value

