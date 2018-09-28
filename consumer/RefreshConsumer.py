# -*- coding: UTF-8 -*-

import threading
import MySQLdb
import SimpleHttpClient
import RefundConsumer

class ShowCommentTipsInfoCleaner:
    def __init__(self):
        self.req = SimpleHttpClient.SimpleHttpClient()
        # self.clean_url = "http://test.mwoperation.meiweishenghuo.com/api/probe/cleanBalance"
        self.clean_url = "http://st.mwoperation.meiweishenghuo.com/2b/consumer/refund"
        # db = MySQLdb.connect('101.200.47.196', 'root', 'hcxy_1326!!', 'mwvendor', 3306, charset='utf8')
        db = MySQLdb.connect('127.0.0.1', 'root', 'pass123', 'test', 3306, charset='utf8')
        self.cursor = db.cursor()

    def request_info(self, consumer_id):
        # req = SimpleHttpClient.SimpleHttpClient()
        r = self.req.get("http://st.mwoperation.meiweishenghuo.com/2b/consumer/getRefundInfo", {"consumerId": consumer_id})
        return r.text

    def start(self):
        sql = "select id from only_recharge"
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        print "results %d " % len(results)
        amount = 0
        for row in results:
            consumer_id = row[0]
            result = self.request_info(consumer_id)
            print "consumer %s = %s" % (consumer_id, result)
            r = self.req.get(self.clean_url, {"consumerId": consumer_id})
            amount = amount + 1
            print "amount = %d , consumer %s = %s" % (amount, consumer_id, r.text)

    def refund(self, consumer_id):
        r = self.req.get("http://st.mwoperation.meiweishenghuo.com/2b/consumer/refund", {"consumerId": consumer_id})
        return r.text



cleaner = ShowCommentTipsInfoCleaner()
s = cleaner.refund("8d56986d-5c2f-46e9-a9e3-5b3ce4adc8bf")
print s


