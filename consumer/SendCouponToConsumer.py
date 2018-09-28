# -*- coding: UTF-8 -*-

import MySQLdb
import SimpleHttpClient


def send_coupon():
    db = MySQLdb.connect('101.200.47.196', 'root', 'hcxy_1326!!', 'mwvendor', 3306, charset='utf8')
    cursor = db.cursor()
    sql = """SELECT cat.consumer_id FROM consumer_activity_trace cat JOIN mw_order o ON cat.object_id = o.id WHERE o.vendor_id NOT IN ("10e059ea-a09d-4ebe-a4b3-2dcfd1f06d77", "7c2d236b-dbdb-4d3d-9b4f-171fc7c74265", "84864b78-3b38-4211-97e4-30a5cd3e1e2d", "a2279496-c980-4c2f-a430-288826cec9ba", "48af970f-9b43-489f-ba8c-f116bb645ad2", "235574b6-a483-4896-b585-e97036549848", "e503464a-30ce-4879-b487-99d6b7f58f31", "2a759a45-5c0c-4358-96a8-f32ba4d50c06", "46b4b8ed-3e94-4bf4-8d31-4fa03f40d94b", "392828f9-9c11-4d3c-ab00-115dbdb35a09", "1bf69cd8-5e00-4932-b365-2f857311d215", "aa4b417c-2519-4836-9c9c-fba67369b33a", "48fbc953-e00b-4664-b95c-d23b20f162c7", "4b09a1b8-926d-4b6f-82f8-8dd52753e462", "1d2c8a41-a244-49f9-b5a0-983fd75d91ea", "9bcf960e-9d50-4e76-9ea3-215d4253cf86", "d706273f-3c90-49f6-b14d-396c6fcc7550", "4fde6788-1895-452f-9495-7fe2103e97d1", "34a8866b-1632-45cc-98b9-05a8d0f89cad", "6a20e6a7-90fe-4c13-b3ef-7136d85e7ff7", "c054b8e7-d5e5-45e6-9289-0bc558f66d44", "ca5c0095-9a36-402f-be5e-5099f56e3e1b", "a47867a2-5a9a-4201-84e4-1622bc1f5cad", "d1ca6eac-12c8-4356-9971-a221e81721be", "6d67edbe-fccd-48ac-ad93-0dc70bb2cf64", "93035278-eb5c-433d-a206-2b6cc444d555", "defa1d6c-cfc3-4f30-8fd5-0ddcdde6e322", "37a5bd0a-cbb2-45d7-8f03-f13553e91db3", "2b4c3fc2-1f8b-4ba0-8ea5-24e8e32d61df", "387546ac-8c72-4082-a569-f9fff3a28b9f", "0f60cfd7-bd92-44cf-99ba-27f32e040c05", "fd7fbf31-8c2a-4a28-a740-8b3d47ce213a") AND date(cat.add_time) >= date("2018-04-02") GROUP BY cat.consumer_id;"""
    cursor.execute(sql)
    consumer_ids = cursor.fetchall()
    req = SimpleHttpClient.SimpleHttpClient("9e2402ba-6703-11e7-a5fa-9801a79f70e5_e4bdb66c735b4ca4bd397f3de877b645")
    for consumer_id in consumer_ids:
        r = req.get("http://st.mwtoc.meiweishenghuo.com/api/probe/deleteActivityTrace", {"consumerId": consumer_id[0]})
        print r.text


# send_coupon()