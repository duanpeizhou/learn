# -*- coding: UTF-8 -*-

from mysql.online import MySQL
import uuid

db = MySQL()

def handle(employee_id):
    total_sql = "select ifnull(sum(order_price),0) from mw_order where order_status in (5,10) and cover_id in (select id from cover where operate_bd= '%s');" % employee_id
    total_rows = db.get_data_by_sql(total_sql)
    total_value = total_rows[0][0]

    un_income_sql = "select ifnull(sum(order_price),0) from mw_order where is_transfer = 0 and out_time >= '2018-12-12 00:00:00' and order_status in (5,10) and cover_id in (select id from cover where operate_bd= '%s')" % employee_id
    un_income_rows = db.get_data_by_sql(un_income_sql)
    un_income_value = un_income_rows[0][0]

    un_transfer_sql = "select ifnull(sum(order_price),0) from mw_order where is_transfer = 0 and out_time < '2018-12-20 00:00:00' and order_status in (5,10) and cover_id in (select id from cover where operate_bd= '%s')" % employee_id
    un_transfer_rows = db.get_data_by_sql(un_transfer_sql)
    un_transfer_value = un_transfer_rows[0][0]

    transfer_sql = "select ifnull(sum(value),0) from withdraw_cash_record where status = 2 and employee_id = '%s';" % employee_id
    transfer_rows = db.get_data_by_sql(transfer_sql)
    transfer_value = transfer_rows[0][0]

    sum_total_value = (float(transfer_value) + float(un_income_value) + float(un_transfer_value))
    subs = float(total_value) - sum_total_value
    print "employee_id = %s , total_value = %f, un_income_value = %f,un_transfer_value=%f,transfer_value=%f,subs = %f" % \
              (employee_id, total_value, un_income_value, un_transfer_value, transfer_value, subs)


def un_transfer(trader_id, employee_id):
    un_transfer_sql = "select ifnull(sum(order_price),0) from mw_order where is_transfer = 0 and out_time < '2018-12-20 00:00:00' and order_status in (5,10) and cover_id in (select id from cover where operate_bd= '%s')" % employee_id
    un_transfer_rows = db.get_data_by_sql(un_transfer_sql)
    un_transfer_value = un_transfer_rows[0][0]
    # print un_transfer_value
    if un_transfer_value == 0:
        return

    record_id = uuid.uuid1()

    trader_balance_record_insert_sql = "INSERT INTO `trader_balance_record` (`id`, `trader_id`, `record_time`, `settlement_date`, `value`, `old_balance`, `new_balance`, `expense_type`) " \
                                       "VALUES ('%s', '%s', now(), '2018-12-19', %0.2f, 0, %0.2f, 1);" \
                                       % (record_id, trader_id, un_transfer_value, un_transfer_value)

    print trader_balance_record_insert_sql

    joining_trader_balance_update_sql = "update joining_trader set balance = %0.2f where employee_id = '%s';" % (un_transfer_value , employee_id)
    print joining_trader_balance_update_sql

    un_transfer_orders = "select id from mw_order where is_transfer = 0 and out_time < '2018-12-20 00:00:00' and order_status in (5,10) and cover_id in (select id from cover where operate_bd= '%s')" % employee_id
    order_id_rows = db.get_data_by_sql(un_transfer_orders)
    for order_id in order_id_rows:
        inward_order_relation_insert_sql = "INSERT INTO `inward_order_relation` (`order_id`, `balance_record_id`) " \
                                       "VALUES ('%s', '%s');" % (order_id[0], record_id)
        print inward_order_relation_insert_sql


def main():
    rows = db.get_data_by_sql("select id,employee_id from joining_trader")
    for row in rows:
        un_transfer(row[0], row[1])


main()