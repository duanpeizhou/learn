# -*- coding: UTF-8 -*-
import SimpleHttpClient
from mysql.online import MySQL

db = MySQL()

http = SimpleHttpClient.SimpleHttpClient("9e2402ba-6703-11e7-a5fa-9801a79f70e5_498129b4-29ae-41c5-b021-9e0b6de0b53f")

# rows = db.get_data_by_sql("select id from consumer where is_vip = 0 and subscribe_weixin = 1 and phone_num is not null;")

# for row in rows:
#     param = {"consumerId": row[0], "status": 1}
#     r = http.get("http://st.mwtoc.meiweishenghuo.com/api/probe/cleanConsumerVip", param)
#     print r.text
