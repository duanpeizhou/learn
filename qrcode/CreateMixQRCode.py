# -*- coding: UTF-8 -*-
import qrcode
from mysql.online import MySQL

#https://github.com/lincolnloop/python-qrcode/wiki
#https://pypi.org/project/qrcode/5.1/#files

def main():
    db = MySQL()
    sql = """select id,vendor_num from vendor where serial_no in (
"861529045882012"
,"861529045862964"
,"861529045928559"
,"861529045901788"
,"861529045881915"
,"861529045847130"
,"861529045882269"
,"861529045848906"
,"861529043088778"
,"861529045884380"
)"""
    rows = db.get_data_by_sql(sql)
    for row in rows:
        createQRCode(row[0], row[1])

    print "完成"



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

