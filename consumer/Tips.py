# -*- coding: UTF-8 -*-

import SimpleHttpClient
from mysql.online import MySQL

db = MySQL()
req = SimpleHttpClient.SimpleHttpClient("9e2402ba-6703-11e7-a5fa-9801a79f70e5_cdde1eae-479b-4dc4-a2f0-2a3a492bf042")


def request():
    rows = db.get_data_by_sql("""select consumer_id from mw_order
where order_status = 5 
and order_type = 2 
and order_price > 50
and date(pay_time) > "2018-07-04";""")
    for consumer_id in rows:
        re = req.get("http://st.mwoperation.meiweishenghuo.com/api/probe/sendRechargeCoupon", {"consumerId": consumer_id[0]})
        print re.text;


# request()

def send(cover_id):
    re = req.get("http://st.mwoperation.meiweishenghuo.com/api/probe/sendHeavenCoupon", {"coverId": cover_id})
    print re.text;


