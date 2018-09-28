# -*- coding: UTF-8 -*-

from mysql.test import MySQL
import SimpleHttpClient

http = SimpleHttpClient.SimpleHttpClient("9e2402ba-6703-11e7-a5fa-9801a79f70e5_498129b4-29ae-41c5-b021-9e0b6de0b53f")

db = MySQL()


def execute():
    order_ids = db.get_data_by_sql("select id from mw_order where order_status = 5 limit 100,900")
    for id in order_ids:
        result = http.get("http://test.mwtoc.meiweishenghuo.com/api/probe/saleData",{"orderId":id[0],"saleStatus":1})
        print result.text


execute()


