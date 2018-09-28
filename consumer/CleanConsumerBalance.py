# -*- coding: UTF-8 -*-

import threading
import MySQLdb
import SimpleHttpClient
import RefundConsumer

class CleanConsumerBalance:

    def __init__(self):
        self.req = SimpleHttpClient.SimpleHttpClient()
        self.clean_url = "http://st.mwoperation.meiweishenghuo.com/api/probe/cleanBalance"
        # self.clean_url = "http://st.mwoperation.meiweishenghuo.com/api/probe/order2ConsumerRecord"
        db = MySQLdb.connect('101.200.47.196', 'root', 'hcxy_1326!!', 'mwvendor', 3306,charset='utf8')
        # db = MySQLdb.connect('47.95.232.160', 'root', 'pass123', 'Order2BalanceTest', 3306, charset='utf8')
        self.cursor = db.cursor()
        self.amount = 0
        self.refund = RefundConsumer.refund_ecard_consumer_ids

    def start(self, start):
        sql = "select consumer_id from ecard where status = 2 and balance > 0 group by consumer_id limit %d , 500" % start
        print sql
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        self.amount = self.amount + len(results)
        print "result length = %d" % len(results)
        print "done %d" % self.amount
        try:
            t = threading.Thread(target=self.clean_consumers, args=(results, ))
            print t
            t.start()
        except:
            print "Error: unable to start thread"

    def clean_consumers(self, arr):
        for row in arr:
            consumer_id = row[0]
            print consumer_id
            if consumer_id not in self.refund:
                result = self.req.get(self.clean_url, {"consumerId": consumer_id})
                print "consumerId %s , result %s " % (consumer_id, result.text)


    def main(self):
        index = 0
        begin = 0
        while begin <= self.amount:
            begin = index * 500
            self.start(begin)
            index = index + 1

clean = CleanConsumerBalance()
# clean.main()


