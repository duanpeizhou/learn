# -*- coding: UTF-8 -*-

from mysql.online import MySQL

db = MySQL()

def handle(employee_id):
    total_sql = "select ifnull(sum(order_price),0) from mw_order where order_status in (5,10) and cover_id in (select id from cover where operate_bd= '%s');" % employee_id
    total_rows = db.get_data_by_sql(total_sql)
    total_value = total_rows[0][0]

    un_income_sql = "select ifnull(sum(order_price),0) from mw_order where is_transfer = 0 and out_time >= '2018-12-12 00:00:00' and order_status in (5,10) and cover_id in (select id from cover where operate_bd= '%s')" % employee_id
    un_income_rows = db.get_data_by_sql(un_income_sql)
    un_income_value = un_income_rows[0][0]

    un_transfer_sql = "select ifnull(sum(order_price),0) from mw_order where is_transfer = 0 and out_time < '2018-12-12 00:00:00' and order_status in (5,10) and cover_id in (select id from cover where operate_bd= '%s')" % employee_id
    un_transfer_rows = db.get_data_by_sql(un_transfer_sql)
    un_transfer_value = un_transfer_rows[0][0]

    transfer_sql = "select ifnull(sum(value),0) from withdraw_cash_record where status = 2 and employee_id = '%s';" % employee_id
    transfer_rows = db.get_data_by_sql(transfer_sql)
    transfer_value = transfer_rows[0][0]

    sum_total_value = (float(transfer_value) + float(un_income_value) + float(un_transfer_value))
    subs = float(total_value) - sum_total_value
    print "employee_id = %s , total_value = %f, un_income_value = %f,un_transfer_value=%f,transfer_value=%f,subs = %f" % \
              (employee_id, total_value, un_income_value, un_transfer_value, transfer_value, subs)


def main():
    rows = db.get_data_by_sql("select employee_id from withdraw_cash_record group by employee_id;")
    for row in rows:
        handle(row[0])

handle('146030bb-7bcb-488f-8f64-fe1282ab81e2')
