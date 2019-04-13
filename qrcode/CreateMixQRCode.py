# -*- coding: UTF-8 -*-
import qrcode
from mysql.online import MySQL

def main():
    db = MySQL()
    rows = db.get_data_by_sql("select id,vendor_num from vendor where vendor_num between 1000553 and 1000562")
    for row in rows:
        createQRCode(row[0], row[1])

    print "生成数量 %d" % rows.len



def createQRCode(vendor_id, name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=20,
        border=0,
    )
    data = "https://ttmwsh.meiweishenghuo.com/weixin/?vendorId=%s" % vendor_id
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    path = "/Users/shengrui/Desktop/png/%s.png" % name
    img.save(path)


main()

