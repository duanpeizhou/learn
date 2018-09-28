# -*- coding: UTF-8 -*-

from mysql.online import MySQL

db = MySQL()


def create_sql():
    sql = "select distinct consumer_id from coupon where coupon_template_id = 3 and date(begin_time) = date('2018-06-04');"
    rows = db.get_data_by_sql(sql)
    base_sql = "INSERT INTO `push_consumer_record` (`consumer_id`, `cover_id`, `push_type`, `add_time`, `push_time`) VALUES "
    for row in rows:
        consumer_id = row[0]
        insert_sql = "('%s', NULL, 2, '2018-06-04 10:06:30', '2018-06-04 10:06:30')," % consumer_id
        base_sql += insert_sql
        print insert_sql
    print base_sql


create_sql()