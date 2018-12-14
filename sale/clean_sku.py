# -*- coding: UTF-8 -*-

import SimpleHttpClient
from mysql.online import MySQL

http = SimpleHttpClient.SimpleHttpClient("9e2402ba-6703-11e7-a5fa-9801a79f70e5_498129b4-29ae-41c5-b021-9e0b6de0b53f")

db = MySQL()

rows = db.get_data_by_sql("select id from sku_ranking where cover_id = 'b181f760-a7b3-4a7f-a979-81c761332618'")

# for row in rows:
#     result = http.get("http://st.mwoperation.meiweishenghuo.com/api/probe/updateSkuRanking", {"skuRankingId": row[0]})
#     print result.text

