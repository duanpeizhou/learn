# -*- coding: UTF-8 -*-

import redisConn.RedisUtils
import SimpleHttpClient
import threading
import MySQLdb
import time
import sys


class FixOrderCleaner:

    def __init__(self):
        self.redis_util = redisConn.RedisUtils.RedisUtils()
        self.req = SimpleHttpClient.SimpleHttpClient()
        self.fix_order_url = "http://st.mwoperation.meiweishenghuo.com/2b/order/fixOrderPrice"

    def reqss(self,results):
        for row in results:
            id = row[0]
            result = self.req.get(self.fix_order_url,{"orderId":id})
            print result.text

    def fix_order(self):
        # 打开数据库连接
        db = MySQLdb.connect('101.200.47.196', 'root', 'hcxy_1326!!', 'mwvendor', 3306,charset='utf8')
        # db = MySQLdb.connect("localhost","root","12345678","test",3306,charset='utf8')
        cursor = db.cursor()
        # 使用execute方法执行SQL语句
        cursor.execute("select id from mw_order mo where order_status in (3,5,10) and order_value = (select sum(group_value) from mw_order_detail where order_id = mo.id) "
                       "and order_price != (select sum(group_price) from mw_order_detail where order_id = mo.id) and discount_value is not null")
        # 获取所有记录列表
        results = cursor.fetchall()
        index = 0
        page = 1000
        while(index * page < len(results)):
            start = index * page
            end = (index + 1) * page
            index = index + 1
            print start
            print end
            print "========="
            print results[start:end]
            temp = list(results[start:end])
            threading.Thread(target=self.reqss,args=(temp,)).start()

    def test(self):
        ss = [1,2,3,4,5,6,7,8,9,0,11]
        index = 0
        page = 2
        while(index * page < len(ss)):
            start = index * page
            end = (index+1) * page
            index = index + 1
            print ss[start:end]
            temp = ss[start:end]
            threading.Thread(target=self.tests(ss[start:end])).start()

    def tests(self,res):
        print res

fixOrder = FixOrderCleaner()

fixOrder.fix_order()

