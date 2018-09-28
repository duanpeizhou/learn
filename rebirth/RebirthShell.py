# -*- coding: UTF-8 -*-
from mysql.test import MySQL

db = MySQL()

def execute(open_id):
    sql = "update consumer set phone_num =   unix_timestamp(now()) where open_id = '';"
    db.get_data_by_sql()