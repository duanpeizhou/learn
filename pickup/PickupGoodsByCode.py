# -*- coding: UTF-8 -*-

import MySQLdb

import SimpleHttpClient


def pick_up_goods(order_id):
    req = SimpleHttpClient.SimpleHttpClient('9e2402ba-6703-11e7-a5fa-9801a79f70e5_d296cc6eeb864d8ba6c05a0e5f66cc16')
    r = req.get('http://test.mwtoc.meiweishenghuo.com/api/probe/pickUpCode', {"orderId": order_id})
    print r.text


def main(pick_up_code):
    pick_up_code = str.upper(pick_up_code)
    print(pick_up_code)
    db = MySQLdb.connect("47.95.232.160", "root", "pass123", "daily_data", 3306, charset='utf8')
    cursor = db.cursor()
    sql = "select id from mw_order where pick_up_code = '%s' order by order_time desc limit 1;" % pick_up_code
    cursor.execute(sql)
    r = cursor.fetchone()
    order_id = r[0]
    pick_up_goods(order_id)


main("4b4c58")
main("b49c36")

"中达大厦一层旋转售货机", "谷泰滨江大厦30号机器", "谷泰滨江92号机器", "清华科技园创业大厦1楼大厅", "软件园云基地CD座1层南门", "京仪科技D座大厅", "花园坊A2楼", \






