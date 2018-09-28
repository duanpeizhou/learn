# -*- coding: UTF-8 -*-
import threading
import thread
import MySQLdb
import SimpleHttpClient
import sys

class CleanConsumerTrace:

    def __init__(self):
        self.req = SimpleHttpClient.SimpleHttpClient()
        self.fix_order_url = "http://st.mwoperation.meiweishenghuo.com/api/probe/cleanOldTrace"
        db = MySQLdb.connect('101.200.47.196', 'root', 'hcxy_1326!!', 'mwvendor', 3306,charset='utf8')
        cursor = db.cursor()

    def start(self, start):
        # db = MySQLdb.connect('47.95.232.160', 'root', 'pass123', 'daily_data', 3306,charset='utf8')
        db = MySQLdb.connect('101.200.47.196', 'root', 'hcxy_1326!!', 'mwvendor', 3306,charset='utf8')
        cursor = db.cursor()
        sql = "select distinct consumer_id from mw_order limit %d , 1000" % start
        print sql
        cursor.execute(sql)
        results = cursor.fetchall()
        try:
            thread.start_new_thread(self.clean_consumer_trace, (results, ))
        except:
            print "Error: unable to start thread"

    def clean_consumer_trace(self, arr):
        for row in arr:
            consumer_id = row[0]
            result = self.req.get(self.fix_order_url, {"consumerId": consumer_id})
            print result.text

    def main(self):
        index = 13
        while 1:
            begin = index * 1000
            self.start(begin)
            index = index + 1


clean = CleanConsumerTrace()
clean.main()
threading._sleep(1000000000000)

