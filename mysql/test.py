# -*- coding: UTF-8 -*-
import MySQLdb


class MySQL:
    def __init__(self, db_name='daily_data'):
        db = MySQLdb.connect('47.95.232.160', 'root', 'pass123', db_name, 3306, charset='utf8')
        # db = MySQLdb.connect('47.95.232.160', 'root', 'pass123', 'mwvendor_data', 3306, charset='utf8')
        self.db = db

    def get_data_by_sql(self, sql):
        print sql
        cursor = self.db.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        # cursor.close()
        return result



