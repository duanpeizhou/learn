# -*- coding: UTF-8 -*-

import time

import MySQLdb

import SimpleHttpClient


def get_phone_nums(index):
    db = MySQLdb.connect('101.200.47.196', 'root', 'hcxy_1326!!', 'mwvendor', 3306, charset='utf8')
    cursor = db.cursor()
    sql = "select open_id from consumer where open_id like 'oksD41%%' limit %d,200" % index
    print sql
    cursor.execute(sql)
    phone_nums = []
    for phone in cursor.fetchall():
        phone_nums.append(phone[0])
    return phone_nums


req = SimpleHttpClient.SimpleHttpClient("9e2402ba-6703-11e7-a5fa-9801a79f70e5_cee20b86-cc4b-4c25-ab32-0d727ce08554")
# req = SimpleHttpClient.SimpleHttpClient("9e2402ba-6703-11e7-a5fa-9801a79f70e5_e2c58056-af28-4d0f-ad63-3ef336c1a492")

def mass_send_sms(phone_nums):
    if len(phone_nums) == 0 :
        return
    param = {
        "from_appid": "wx6ad6df1ceb33e4e3",
        "openid_list": phone_nums
    }
    # print json.dumps(param)
    url = "http://st.mwoperation.meiweishenghuo.com/api/probe/changeOpenId"
    r = req.post(url, param)
    print r.text


def batch_send():
    page_size = 200;
    page_no = 1
    phone_num_len = 1
    while phone_num_len != 0:
        index = (page_no - 1)*page_size
        phones = get_phone_nums(index)
        phone_num_len = len(phones)
        mass_send_sms(phones)
        print page_no
        print phones
        page_no += 1
        time.sleep(2)


batch_send()



