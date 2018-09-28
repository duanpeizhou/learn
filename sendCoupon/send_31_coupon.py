# -*- coding: UTF-8 -*-
import SimpleHttpClient
from mysql.online import MySQL

db = MySQL()
req = SimpleHttpClient.SimpleHttpClient("9e2402ba-6703-11e7-a5fa-9801a79f70e5_fa332b7b-86a5-4861-9b42-dfb738a22da5")
# req = SimpleHttpClient.SimpleHttpClient("9e2402ba-6703-11e7-a5fa-9801a79f70e5_cee20b86-cc4b-4c25-ab32-0d727ce08554")


def request(consumer):
    r = req.get("https://st.mwoperation.meiweishenghuo.com/api/probe/sendMoonCoupon",
                {"consumerId": consumer})
    print r.text



# request("e79670b0-6b2b-4871-8d8b-a82dd5c23309")


def execute():
    sql = """select o.consumer_id from mw_order o
left join cover c on c.id = o.cover_id
where c.city_id = 1
and o.order_status in (3,5,7,10)
and consumer_id in 
(
select distinct consumer_id from consumer c
left join consumer_vip_record r on c.id = r.consumer_id
where c.is_vip = 0
and r.vip_recharge_type = 1
)
group by o.consumer_id
having max(pay_time) < "2018-09-03";"""
    rs = db.get_data_by_sql(sql)
    for consumer_id in rs:
       request(consumer_id[0])

execute()