#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright 2021 Anoyer All Rights Reserved.
# Author: zhihuangliu@foxmail.com
#

__all__ = [
    "load_data",
    "get_all_table_config"
]

import os

from utils.common import read_json_from_file

_global_dict = {}
_global_config = []


def get_cwd():
    return os.getcwd()


def load_data():
    global _global_dict, _global_config
    run_path = get_cwd()
    _global_dict = {}
    _global_config = read_json_from_file("CentralVision.conf")
    for pos, _dict in enumerate(_global_config.get("table_list", [])):
        _global_dict[pos] = _dict
        _global_config["table_list"][pos]["uid"] = pos


def set_value(key, value):
    _global_dict[key] = value


def get_value(key, default_value=None):
    try:
        return _global_dict[key]
    except KeyError:
        return default_value


def get_all_table_config():
    global _global_config
    return _global_config

