#!/usr/bin/python3

import pymysql
import json


if __name__ == "__main__":

    with open("CentralVision.conf", "r") as r:
        config_dict = json.load(r)

    db = pymysql.connect(host=config_dict['host'], user=config_dict['user'], password=config_dict['password'],
                         database=config_dict['database'], charset=config_dict['charset'])
    cursor = db.cursor()

    sql = """
        SELECT * from test
        """
    res = cursor.execute(sql)
    print(cursor.description)
    print(res)

    result = cursor.fetchall()
    data_dict = []
    for field in cursor.description:
        data_dict.append(field[0])
    print(data_dict)
    cursor.close()

    db.close()


