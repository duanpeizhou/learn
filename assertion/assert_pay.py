# -*- coding: UTF-8 -*-
import datetime
import json
import sys
import time
import urllib

import requests

from mysql.test import MySQL

db = MySQL('mwpt')
confirm_pay_url = "http://localhost:5566/2c/order/confirmPay"
notify_pay_result_url = "http://localhost:5566/api/probe/mockPayResult"

header = {
    "pt-open-id": "d77fb1fd-b62e-4560-aad3-e7848ca822b5",
    "Content-Type": "application/json; charset=utf-8",
    "Proxy-Client-IP": "47.95.232.160"
}


building_id = "488fd467-7540-46c0-aa23-5abc040fb248"
delivery_address_id = "c39e7c9f-85f9-4c5a-af0f-48ac82d7b2c9"
customer_1_id = "211b24bd-80e2-4da5-9742-f917dd8d13ad"
goods_1_id = "f7289511-89ba-4efa-8ec2-33f33cd5e391"


def validate_input_param():
    sql = "select name from building where id = '%s'" % building_id
    buildings = db.get_data_by_sql(sql)
    if len(buildings) == 0:
        print "building not exist . id = %s" % building_id
        sys.exit(0)
    print "selected building name = %s" % buildings[0][0]

    da_sql = "select id from delivery_address where id = '%s'" % delivery_address_id
    delivery_addresses = db.get_data_by_sql(da_sql)
    if len(delivery_addresses) == 0:
        print "配送地址不存在 %s" % delivery_address_id
        sys.exit(0)


validate_input_param()

base_param = {
    "buildingId": "488fd467-7540-46c0-aa23-5abc040fb248",
    "deliveryAddressId": "c39e7c9f-85f9-4c5a-af0f-48ac82d7b2c9",
    "formId": "string",
    "isNewPt": 1,
    "payType": 1,
    "goods": []
}


delivery_time = datetime.datetime.now() + datetime.timedelta(days=1)

common_consumer_buy = [{
        "customerId": "211b24bd-80e2-4da5-9742-f917dd8d13ad",
        "deliveryDate": delivery_time.strftime("%Y-%m-%d"),
        "goodsList": [{
            "amount": 1,
            "goodsId": "f7289511-89ba-4efa-8ec2-33f33cd5e391"
        }],
        "supplyTimeType": 2
}]


def print_order_info(pay_action_id):
    pay_action_sql = "select value,pay_status from pay_action where id = '%s'" % pay_action_id
    pay_action_rows = db.get_data_by_sql(pay_action_sql)
    pay_action = pay_action_rows[0]
    print "pay_action 支付金额:%.2f  支付状态:%d" % (pay_action[0], pay_action[1])
    mw_order_sql = "select init_price,current_price,discount_value,delivery_price,order_status,id " \
                   "from mw_order where pay_action_id = '%s'" % pay_action_id
    mw_order_rows = db.get_data_by_sql(mw_order_sql)
    print "-----------订单开始------------"
    for mw_order in mw_order_rows:
        print "  init_price:%.2f  current_price:%.2f  discount_value:%.2f  delivery_price:%.2f  order_status:%d" % \
              (mw_order[0], mw_order[1], mw_order[2], mw_order[3], mw_order[4])
        order_detail_sql = "select * from mw_order_detail where order_id = '%s'" % mw_order[5]
        order_detail_list = db.get_data_by_sql(order_detail_sql)
        for order_detail in order_detail_list:
            print order_detail
    print "-----------订单结束------------"


def notify_pay_result(trade_no):
    param = {"tradeNo": trade_no, "transactionId": time.time()}
    r = requests.get(notify_pay_result_url, params=urllib.urlencode(param), headers=header)
    print r.text


def assert_pay():
    buy_num_arr = [1]
    for buy_num in buy_num_arr:
        common_consumer_buy[0]["goodsList"][0]["amount"] = buy_num
        base_param["goods"] = common_consumer_buy
        confirm_pay_result = requests.post(url=confirm_pay_url, data=json.dumps(base_param), headers=header)
        print confirm_pay_result.text
        result = json.loads(confirm_pay_result.text)
        if result["status"] == 1:
            notify_pay_result(result["data"]["tradeNo"])


# assert_pay()

print_order_info("ab634273-b79f-4f07-8338-d8c6e5c123f7")

notify_pay_result("1538189647922469375802")