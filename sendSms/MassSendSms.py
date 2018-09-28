# -*- coding: UTF-8 -*-
import SimpleHttpClient
import MySQLdb
import time


def get_phone_nums(index):
    db = MySQLdb.connect('101.200.47.196', 'root', 'hcxy_1326!!', 'mwvendor', 3306, charset='utf8')
    cursor = db.cursor()
    sql = "select distinct phone_num from ccov where cover_name = '建金中心1层(金隅启迪孵化器)' and date(order_time) > date('2018-05-07') and phone_num is not null limit %d,200" % index
    print sql
    cursor.execute(sql)
    phone_nums = []
    for phone in cursor.fetchall():
        phone_nums.append(phone[0])
    return phone_nums


def mass_send_sms(phone_nums):
    if len(phone_nums) == 0 :
        return
    req = SimpleHttpClient.SimpleHttpClient("9e2402ba-6703-11e7-a5fa-9801a79f70e5_cee20b86-cc4b-4c25-ab32-0d727ce08554")
    param = {
        "content": "客官您好，非常抱歉上周五（5.25日）的设备故障给您带来的用餐不便，为了表达我们的歉意，现已给您发放一张满10减3的购餐红包，请注意查收，感谢您对美味生活的支持。ps：现在设备已经恢复正常运营，您可以放心订餐～http://y0.cn/mwsh",
        "phoneNumList": phone_nums
    }
    # print json.dumps(param)
    url = "http://st.mwoperation.meiweishenghuo.com/api/probe/massSend"
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


# batch_send()

phone_nums = [
 "13761008957", "15262426781", "13816007768", "18317174589", "15666793271", "17612150291", "18939719336", "13764021425", "13386180190"
]
mass_send_sms(phone_nums)