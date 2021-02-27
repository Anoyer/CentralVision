#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright 2021 Anoyer All Rights Reserved.
# Author: zhihuangliu@foxmail.com
#

__all__ = [
    "start",
    "select",
    "terminate"
]

import pymysql
import json

from utils import mysql_global_setting
from utils.mysql_global_setting import load_data

_sql = None


class MySql:
    def __init__(self):
        self.date_base = None
        try:
            self.date_base = pymysql.connect(host=mysql_global_setting.get_value('host'),
                             user=mysql_global_setting.get_value('user'),
                             password=mysql_global_setting.get_value('password'),
                             database=mysql_global_setting.get_value('database'),
                             charset=mysql_global_setting.get_value('charset'))
            self.cursor = self.date_base.cursor()
        except Exception as e:
            print(e)

    def select(self, cmd):
        if self.date_base is None:
            return "mysql connect error!"
        self.cursor.execute(cmd)
        result = self.cursor.fetchall()
        return result

    def terminate(self):
        if self.date_base is None:
            return
        self.cursor.close()
        self.date_base.close()


def start():
    global _sql
    _sql = MySql()


def terminate():
    global _sql
    _sql.terminate()


def select(cmd):
    global _sql
    return _sql.select(cmd)



