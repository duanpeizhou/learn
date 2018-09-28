# -*- coding: UTF-8 -*-
import MySQLdb
import datetime


class OrderData:
    def __init__(self):
        pass


    def get_all_cover_out_data(self, date_str, hour):
        print "=========出餐时间 %s==============" % (date_str)
        sql = "SELECT COUNT(1) AS cc , COUNT(buy_type = 2 OR NULL) AS reserve , COUNT(buy_type IN (1, 5) OR NULL) AS normal, cover.nick_name ,vendor.vendor_num, date(ifnull(reserve_date, pay_time)) FROM mw_order mo JOIN vendor ON vendor.id = mo.vendor_id JOIN cover ON cover.id = mo.cover_id WHERE vendor.vendor_model BETWEEN 1 AND 4 AND mo.order_status IN (3, 5, 7, 9, 10) AND (mo.buy_type IN (1, 5) AND date(mo.pay_time) = date('%s') and hour(mo.pay_time) < %d ) AND mo.order_type = 1 AND cover.nick_name IN ( '海龙大厦',  '金源商务中心B区大厅',  '汇众大厦',  '标厂科技园',  '清科创业大厦',  '京仪科技孵化器',  '计算机研究所98号',  '北环中心B1层',  '科贸大厦',  '金隅启迪孵化器1层',  '京蒙高科',  '光正中心',  '北京卓众出版有限公司',  '青云当代',  '博泰职业中心B座',  '国永融通大厦108号',  '国永融通大厦23',  '龙辉大厦',  '品友互动68号机',  '品友互动135号机',  '建磊国际102号',  '建磊国际61号',  '云基地集团',  '健康智谷一层',  '健康智谷10层',  '天亿集团',  '盈都大厦',  '顺和财富中心',  '中京集团127号',  '天博中润1',  '科贸9层',  '科贸10层',  '慈云寺桥44号',  '慈云寺桥50号',  '桑普大厦',  '阳明广场',  '云鸟科技二层',  '云鸟科技三层',  '文津公寓' ) GROUP BY cover.nick_name ORDER BY cc DESC;" % (date_str, hour)
        # 打开数据库连接
        db = MySQLdb.connect('101.200.47.196', 'root', 'hcxy_1326!!', 'mwvendor', 3306,charset='utf8')
        # db = MySQLdb.connect("localhost","root","12345678","test",3306,charset='utf8')
        cursor = db.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

        for row in rows:
            row = row + (hour,)
            print "%d %d %d %s %s %s %s" % row


    def get_period(self):
        hours = (10, 11, 12, 17, 18, 20, 21)
        today = datetime.date.today()
        start_date = datetime.date(2018, 1, 18)
        one_day = datetime.timedelta(days=1)
        while start_date <= today:
            # print start_date
            for hour in hours:
                od.get_all_cover_out_data(start_date,hour)
            start_date += one_day


od = OrderData()
# od.get_all_cover_out_data('2018-03-12')
od.get_period()


