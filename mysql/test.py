# -*- coding: UTF-8 -*-
import MySQLdb


class MySQL:

    def __init__(self, db_name='daily_data'):
        self.db_name = db_name

    def get_data_by_sql(self, sql):
        print sql
        db = MySQLdb.connect('47.95.232.160', 'root', 'pass123', self.db_name, 3306, charset='utf8')
        cursor = db.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        db.commit()
        cursor.close()
        db.close()
        return result



