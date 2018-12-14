# -*- coding: UTF-8 -*-

from mysql.online import MySQL

db = MySQL()

employee_id_2_time = {}


def handle(record, num):
    withdraw_cash_record_id = record[0]
    employee_id = record[1]
    commit_time = record[2]
    withdraw_value = record[3]

    # get_cover_list_sql = "select sum(order_price) from mw_order where cover_id in (select id from cover where operate_bd = '%s') " \
    #                      "and order_status = 5 and pay_time < '%s'" % (employee_id, commit_time)

    get_order_ids_sql = "select id,min(out_time),max(out_time) from mw_order where cover_id in (select id from cover where operate_bd = '%s') " \
                    "and order_status = 5 and pay_time < '%s'" % (employee_id, commit_time)

    if employee_id_2_time.has_key(employee_id):
        end_time = "and pay_time > '%s'" % employee_id_2_time[employee_id]
        # get_cover_list_sql = get_cover_list_sql + end_time
        get_order_ids_sql = get_order_ids_sql + end_time

    employee_id_2_time[employee_id] = commit_time

    # total = db.get_data_by_sql(get_cover_list_sql)

    # print get_cover_list_sql

    order_ids = db.get_data_by_sql(get_order_ids_sql)

    # update_order_sql = "update mw_order set is_transfer = 1 where id in ("
    for order_id in order_ids:
        print "update withdraw_cash_record set trade_begin_time = '%s',trade_end_time = '%s' where id = '%s' ;" % (order_id[1], order_id[2],withdraw_cash_record_id)
        # update_order_sql = update_order_sql + "'" + order_id[0] + "',"
        # print "INSERT INTO `withdraw_order_relation` (`order_id`, `withdraw_cash_record_id`) VALUES ('%s', '%s');" % (order_id[0], record[0])

    # l = len(update_order_sql) - 1
    # update_order_sql = update_order_sql[0:l] + ");"
    # print update_order_sql
    # if record[3] != total[0][0]:
    #     print "============ %s" % withdraw_cash_record_id
    #
    # print "num = %d withdraw value  %s=%s order value " % (num, record[3], total[0][0])


def main():
    num = 1
    records = db.get_data_by_sql("select id, employee_id, commit_time, value from withdraw_cash_record order by commit_time")
    for record in records:
        handle(record, num)
        num = num + 1


main()


