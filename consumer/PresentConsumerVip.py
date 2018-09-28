# -*- coding: UTF-8 -*-
import SimpleHttpClient
import MySQLdb


req = SimpleHttpClient.SimpleHttpClient("9e2402ba-6703-11e7-a5fa-9801a79f70e5_e4bdb66c735b4ca4bd397f3de877b645")


def present_vip(consumer_id):
    r = req.get("http://st.mwoperation.meiweishenghuo.com/api/probe/presentVip", {"consumerId": consumer_id})
    print r.text


def get_present_vip_consumer():
    db = MySQLdb.connect('101.200.47.196', 'root', 'hcxy_1326!!', 'mwvendor', 3306,charset='utf8')
    # db = MySQLdb.connect('47.95.232.160', 'root', 'pass123', 'Order2BalanceTest', 3306, charset='utf8')
    cursor = db.cursor()
    sql = "select sum(order_price) s,consumer_id,count(id) from mw_order where order_status in (3,5,10) and order_type = 1 and date(order_time) between date('2018-01-01') and date('2018-01-31') and is_pack = 0 group by consumer_id desc having s > 200"
    cursor.execute(sql)
    consumers = cursor.fetchall()
    for consumer in consumers:
        consumer_id = consumer[1]
        present_vip(consumer_id)


# get_present_vip_consumer()