# -*- coding: UTF-8 -*-

import threading
import MySQLdb
import SimpleHttpClient
import RefundConsumer


class CleanConsumerBalance:
    def __init__(self):
        self.req = SimpleHttpClient.SimpleHttpClient()
        # self.clean_url = "http://test.mwoperation.meiweishenghuo.com/api/probe/cleanBalance"
        self.clean_url = "http://localhost:8080/api/probe/order2ConsumerRecord"
        db = MySQLdb.connect('101.200.47.196', 'root', 'hcxy_1326!!', 'mwvendor', 3306, charset='utf8')
        # db = MySQLdb.connect('47.95.232.160', 'root', 'pass123', 'online20180118', 3306, charset='utf8')
        self.cursor = db.cursor()
        self.amount = 0
        self.records = RefundConsumer.refund_ecard_consumer_ids

    def start(self, start):
        sql = "select distinct consumer_id from ecard where consumer_id is not null limit %d , 500" % start
        print sql
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        self.amount = self.amount + len(results)
        self.clean_consumers(results)

    def clean_consumers(self, arr):
        for row in arr:
            consumer_id = row[0]
            denomination_sql = "select sum(denomination) d,sum(balance) b from ecard where consumer_id = '%s'" % consumer_id
            self.cursor.execute(denomination_sql)
            row = self.cursor.fetchall()[0]
            denomination = float(row[0])
            balance = float(row[1])

            consume_order_total_sql = "select ifnull(sum(order_price),0) from mw_order where  consumer_id = '%s' and trade_type = 4 and order_status in (3,5,10)" % consumer_id
            self.cursor.execute(consume_order_total_sql)
            consume_order_total = self.cursor.fetchall()[0][0]

            # consume_record_total_sql = "select ifnull(sum(value),0) from ecard_consume_record where ecard_id in (select id from ecard where consumer_id = '%s' )" % consumer_id
            # self.cursor.execute(consume_record_total_sql)
            # consume_record_total = self.cursor.fetchall()[0][0]

            if denomination != (balance + float(consume_order_total)):
                if consumer_id not in self.records:
                    print "order %s" % consumer_id

                # if denomination != (balance + consume_record_total):
                #     print "record %s " % consumer_id

    def main(self):
        index = 0
        begin = 0
        while begin <= self.amount:
            begin = index * 500
            self.start(begin)
            index = index + 1



clean = CleanConsumerBalance()
clean.main()


