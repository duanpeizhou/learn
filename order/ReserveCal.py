# -*- coding: UTF-8 -*-
import MySQLdb
import time
import datetime

db = MySQLdb.connect('101.200.47.196', 'root', 'hcxy_1326!!', 'mwvendor', 3306,charset='utf8')
cursor = db.cursor()

vendor_num = (1000348,1000346,1000345,1000342,1000339,1000135,1000127,1000126,1000125,1000121,1000118,1000105,1000104,1000102,1000097,1000083,1000068,1000050,1000044,1000023,1000020,1000019,1000018,1000017,1000016,1000015,1000014,1000012,1000011,1000010,1000009,1000008,1000007,1000005,1000004)

def getFromDBPrice(date):
    print "=============%s================" % date
    sql = "select ven.vendor_num,count(mo.id),round(avg(mo.order_price),2),round(avg(ifnull(dst.rel,mo.order_price)),2) ag from mw_order mo join (select * from vendor where vendor_num in (1000345 , 1000346 , 1000127 , 1000068 , 1000020 , 1000348 , 1000011 , 1000126 , 1000342 , 1000007 , 1000018 , 1000012 , 1000015 , 1000008 , 1000016 , 1000125 , 1000017 , 1000019 , 1000339 , 1000004 , 1000009 , 1000014 , 1000010 , 1000005 , 1000121 , 1000083 , 1000050 , 1000105 , 1000104 , 1000135 , 1000102 , 1000097 , 1000023 , 1000118 , 1000044)) ven on ven.id = mo.vendor_id left join (select round(sum(ecr.value*disc.disco),2) rel,ecr.order_id from ecard_consume_record ecr join (select e.id eid,ifnull(mo.order_price/e.denomination,0) disco from ecard e left join (select * from mw_order where is_pack = 2) mo on e.order_id = mo.id) disc on disc.eid = ecr.ecard_id group by ecr.order_id) dst on dst.order_id = mo.id where ((order_status = 5  and date(out_time) = date('%s')) or (order_status = 10 and date(order_time) = date('%s') and buy_type != 2) or (order_status = 10 and date(reserve_date) = date('%s'))) and mo.is_pack = 0 group by ven.vendor_num order by ven.vendor_num" % (date,date,date)
    cursor.execute(sql)
    results = cursor.fetchall()
    dict={}
    for row in results:
        vendorNum = str(row[0])
        dict[vendorNum] = row

    for vendor in vendor_num:
        if dict.has_key(str(vendor)):
            rows = dict.get(str(vendor))
            print "%s %10s %10s %10s" % (rows[0], rows[1], rows[2], rows[3])
        else:
            print "%s %10s %10s %10s" % (vendor, 0, 0, 0)

def getFromDBReserve(date):
    print "=============%s======预定量==========" % date
    sql = "SELECT ven.vendor_num, COUNT(mo.id) FROM mw_order mo JOIN ( SELECT * FROM vendor WHERE vendor_num IN (1000345, 1000346, 1000127, 1000068, 1000020, 1000348, 1000011, 1000126, 1000342, 1000007, 1000018, 1000012, 1000015, 1000008, 1000016, 1000125, 1000017, 1000019, 1000339, 1000004, 1000009, 1000014, 1000010, 1000005, 1000121, 1000083, 1000050, 1000105, 1000104, 1000135, 1000102, 1000097, 1000023, 1000118, 1000044) ) ven ON ven.id = mo.vendor_id WHERE ((order_status = 5 AND date(out_time) = date('%s')) OR (order_status = 10 AND date(order_time) = date('%s') AND buy_type != 2) OR (order_status = 10 AND date(reserve_date) = date('%s'))) AND is_pack = 0 AND buy_type = 2 GROUP BY ven.vendor_num ORDER BY ven.vendor_num" % (date,date,date)
    cursor.execute(sql)
    results = cursor.fetchall()
    dict_reserve = {}
    for row in results:
        dict_reserve[str(row[0])] = row

    for v in vendor_num:
        if dict_reserve.has_key(str(v)):
            row_reverse = dict_reserve.get(str(v))
            print "%s %10s" % (row_reverse[0], row_reverse[1])
        else:
            print "%s %10s" % (v, 0)

def main():
    i=1
    now = datetime.datetime.now()
    while(i < 57):
        de = 0 - i
        i=i+1
        delta = datetime.timedelta(days=de)
        n_days = now + delta
        da = n_days.strftime('%Y-%m-%d')
        # getFromDBPrice(da)
        getFromDBReserve(da)


main()
# getFromDB('2018-01-23')

