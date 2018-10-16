# -*- coding: UTF-8 -*-
import MySQLdb


class MySQL:
    def __init__(self, db_name='mwvendor'):
        db = MySQLdb.connect('101.200.47.196', 'root', 'ejox_we!xsPvz', db_name, 3306, charset='utf8')
        self.cursor = db.cursor()

    def get_data_by_sql(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result



