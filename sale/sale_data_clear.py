# -*- coding: UTF-8 -*-
import datetime

import SimpleHttpClient
from mysql.online import MySQL
import threading
import json

http = SimpleHttpClient.SimpleHttpClient("9e2402ba-6703-11e7-a5fa-9801a79f70e5_498129b4-29ae-41c5-b021-9e0b6de0b53f")

db = MySQL()


def post_data(sale_data_param):
    # resp = http.post("http://mwoperation.meiweishenghuo.com/2b/data/saleData/clear", sale_data_param)
    resp = http.post("http://test.mwoperation.meiweishenghuo.com:8866/2b/data/saleData/clear", sale_data_param)
    print resp.text


def convert(sale):
    sale_data_param = {
        "vendorId": str(sale[0]), "vendorNum": int(sale[1]), "vendorModel": int(sale[2]),
        "coverId": str(sale[3]), "coverName": sale[4], "provinceId": int(sale[5]),
        "cityId": int(sale[5]), "districtId": int(sale[6]), "groupId": str(sale[7]),
        "groupName": sale[8], "orderId": str(sale[9]), "happenTime": str(sale[10]),
        "buyPrice": float(sale[11]), "productPrice": float(sale[12]), "orderPrice": float(sale[13]),
        "orderValue": float(sale[14]), "consumerId": str(sale[15]), "tocCategory": int(sale[16]),
        "isReserve": int(sale[17]), "storageId": str(sale[18]),
        "isFirstOrder": 0,
        "isVip": 0,
        "saleStatus": 0
    }
    is_first_order_ = is_first_order(sale[15], sale[19])
    is_vip_ = is_vip(sale[15],sale[19])
    sale_data_param["isFirstOrder"] = is_first_order_
    sale_data_param["isVip"] = int(is_vip_)
    if sale[20] == 5 or sale[20] == 10 or sale[20] == 7 or sale[20] == 3:
        sale_data_param["saleStatus"] = 1
    elif sale[20] == 9:
        sale_data_param["saleStatus"] = 3
    if sale[21] == 5:
        sale_data_param["saleStatus"] = 2
    return sale_data_param


def clear_reserve_amount(date):
    sql = """select mo.vendor_id vendor_id,v.vendor_num,v.vendor_model,
              mo.cover_id,c.nick_name,
              c.city_id,c.district_id,modt.group_id,
              gg.group_name, mo.id,ifnull(out_time,order_time) happen_time,
              gg.buy_price,gg.product_price,mo.order_price,
              mo.order_value,mo.consumer_id,gg.toc_category, 
              (CASE WHEN buy_type = 2 THEN 1 ELSE 0 END) AS isReserve,modt.storage_id,
               mo.order_time,mo.order_status,mo.order_type from (
            select * from mw_order where order_status between 3 and 10 and buy_type = 2 
            and order_type = 1 and date(reserve_date) = date(%s)
            ) mo 
            join vendor v on mo.vendor_id = v.id
            join cover c on mo.cover_id = c.id 
            join mw_order_detail modt on mo.id = modt.order_id
            join goods_group gg on modt.group_id = gg.id
            where v.vendor_model between 1 and 3 and gg.toc_category between 8 and 9 and modt.storage_id is not NULL """ % date
    sales = db.get_data_by_sql(sql)
    for sale in sales:
        sale_data_param = convert(sale)
        post_data(sale_data_param)


def clear_normal_amount(date):
    sql = """select mo.vendor_id vendor_id,v.vendor_num,v.vendor_model,mo.cover_id,c.nick_name,c.city_id,c.district_id,modt.group_id,gg.group_name,mo.id,ifnull(out_time,order_time) happen_time,gg.buy_price,gg.product_price,mo.order_price,mo.order_value,mo.consumer_id,gg.toc_category,(CASE WHEN buy_type = 2 THEN 1 ELSE 0 END) AS isReserve,modt.storage_id,mo.order_time,mo.order_status,mo.order_type from (
              select * from mw_order where order_status between 3 and 10 and buy_type in (1,5) and order_type = 1 and date(order_time) = date(%s)
              ) mo 
              join vendor v on mo.vendor_id = v.id
              join cover c on mo.cover_id = c.id 
              join mw_order_detail modt on mo.id = modt.order_id
              join goods_group gg on modt.group_id = gg.id
              where v.vendor_model between 1 and 3 
              and gg.toc_category between 8 and 9
              and modt.storage_id is not null""" % date

    sales = db.get_data_by_sql(sql)
    for sale in sales:
        sale_data_param = convert(sale)
        post_data(sale_data_param)


def clear_out_of_date(date):
    sql = "select v.id,v.vendor_num,v.vendor_model," \
          "c.id,c.nick_name,c.city_id,c.district_id,gg.id," \
          "gg.group_name,record_time,gg.buy_price,gg.toc_category,gg.product_price,storage_id from (select " \
          "storage_id,old_value,vendor_id,record_time from replenishment_record where record_type " \
          "= 2 and date(record_time) = date(%s) and operator = 1) s join goods_group gg " \
          "on s.old_value = gg.id join vendor v on v.id = s.vendor_id join cover c on c.vendor_id " \
          "= v.id;" % date
    rows = db.get_data_by_sql(sql)
    for sale in rows:
        sale_data_param = {
            "vendorId": str(sale[0]), "vendorNum": int(sale[1]), "vendorModel": int(sale[2]),
            "coverId": str(sale[3]), "coverName": sale[4], "provinceId": int(sale[5]),
            "cityId": int(sale[5]), "districtId": int(sale[6]), "groupId": str(sale[7]),
            "groupName": sale[8], "happenTime": str(sale[9]), "buyPrice": float(sale[10]),
            "tocCategory": int(sale[11]), "productPrice": float(sale[12]), "storage_id":str(sale[13]),
            "isFirstOrder": 0,
            "isVip": 0,
            "saleStatus": 3
        }
        post_data(sale_data_param)


def is_vip(consumer_id, order_time):
    date_str = order_time.strftime("'%Y-%m-%d'")
    sql = "select count(id) from consumer_vip_record where date(%s) BETWEEN date(start_time) and date(expire_time) " \
          "and consumer_id = '%s';" % (date_str, consumer_id)
    result = db.get_data_by_sql(sql)
    if result[0] == 0:
        return 0
    else:
        return 1


def is_first_order(consumer_id,pay_time):
    sql = "select id from mw_order where consumer_id = '%s' and order_status in (3,5,7,9,10) and pay_time < '%s' limit 1" % (consumer_id,pay_time)
    result = db.get_data_by_sql(sql)
    if result:
        return 0
    else:
        return 1


def main():
    begin = datetime.datetime(2018, 4, 4)
    end = datetime.datetime(2018, 5, 18)
    delta = datetime.timedelta(days=1)
    while begin <= end:
        date = begin.strftime("'%Y-%m-%d'")
        print date
        clear_reserve_amount(date)
        clear_normal_amount(date)
        clear_out_of_date(date)
        begin = begin + delta


main()








