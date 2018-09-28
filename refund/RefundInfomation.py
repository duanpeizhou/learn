# -*- coding: UTF-8 -*-
import xlwt
import SimpleHttpClient
import MySQLdb
import json


def main():
    db = MySQLdb.connect('127.0.0.1', 'root', 'pass123', 'test', 3306, charset='utf8')
    cursor = db.cursor()
    cursor.execute("select id from only_recharge")
    result = cursor.fetchall()
    book, sheet = create_excel()
    row = 1
    for consumer in result:
        consumer_id = consumer[0]
        refund_info = request_info(consumer_id)
        save_rows(sheet, row, refund_info)
        row = row + 1
    save_excel(book)


def request_info(consumer_id):
    req = SimpleHttpClient.SimpleHttpClient()
    r = req.get("http://st.mwoperation.meiweishenghuo.com/2b/consumer/getRefundInfo", {"consumerId": consumer_id})
    d = json.loads(r.text)
    info = d['data']['items'][0]
    print info
    return info


def create_excel():
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('快消仅充值过的用户退款列表', cell_overwrite_ok=True)
    sheet.write(0, 0, "城市名称")
    sheet.write(0, 1, "用户昵称")
    sheet.write(0, 2, "电话号码")
    sheet.write(0, 3, "账户余额")
    sheet.write(0, 4, "退款金额")
    return book, sheet


def save_rows(sheet, row, param):
    sheet.write(row, 0, param["cityName"])
    sheet.write(row, 1, param["consumerNickName"])
    sheet.write(row, 2, str(param["phoneNum"]))
    sheet.write(row, 3, param["balance"])
    sheet.write(row, 4, param["refund"])


def save_excel(book):
    book.save(r'/Users/shengrui/Desktop/test1.xls')


# main()

# param = {"consumerId": "cb083fda-c56c-411d-b446-f2218412b63e","consumerNickName": "Dava","phoneNum": "13051323520","balance": 0,"refund": 4.77, "coverNickName": "海龙大厦2","cityName": "北京"}
# save_rows(1, param)
