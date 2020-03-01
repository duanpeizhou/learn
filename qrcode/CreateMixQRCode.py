# -*- coding: UTF-8 -*-
import qrcode
from mysql.online import MySQL

#https://github.com/lincolnloop/python-qrcode/wiki
#https://pypi.org/project/qrcode/5.1/#files

def main():
    db = MySQL()
    sql = """select id,vendor_num from vendor where serial_no in (
"32FFD9054D4E383930760451", "51FF70067580505152530267", "48FF6C066666575136441067", "32006D063141333023100143", "48FF6F065184565122212587", "30FF6B063050333553462043", "52FF6F066765505035120767", "48FF76065184565159321887", "56FF77067067495046401667", "54FF6E067087505652290667", "48FF75065184565119371887", "48FF70065184565157241887", "51FF6B067580505111350167", "32FF6B06344D353318531357", "49FF6B065070495231520587", "48FF70065184565133561887", "51FF72065078565538530387"
) order by vendor_num"""
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

