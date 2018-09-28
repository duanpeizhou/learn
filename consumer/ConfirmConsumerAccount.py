# -*- coding: UTF-8 -*-
import MySQLdb
import SimpleHttpClient


class ConfirmConsumerAccount:
    def __init__(self):
        db = MySQLdb.connect('101.200.47.196', 'root', 'hcxy_1326!!', 'mwvendor', 3306, charset='utf8')
        self.cursor = db.cursor()

    def get_charge(self, consumer_id):
        get_charge_sql = "select ifnull(sum(denomination),0) from ecard where order_id is not null and order_id in (select id from mw_order where consumer_id = '%s' and is_pack=2);" % consumer_id
        self.cursor.execute(get_charge_sql)
        charge_amount = self.cursor.fetchone()
        return charge_amount[0]

    def get_bind(self, consumer_id):
        get_bind_sql = "select ifnull(sum(denomination),0) from ecard where source = 1 and ( (consumer_id = '%s') " \
                       "or (id in (select ecard_id from ecard_consume_record where order_id in " \
                       "(select id from mw_order where consumer_id = '%s' and trade_type=4))))" % (consumer_id,consumer_id)
        self.cursor.execute(get_bind_sql)
        bind_amount = self.cursor.fetchone()
        return bind_amount[0]

    def get_consume_order(self, consumer_id):
        get_consumer_order_sql = "select ifnull(sum(order_price),0) from mw_order where consumer_id = '%s' and trade_type = 4 and order_status in (3,5,10)" % consumer_id
        self.cursor.execute(get_consumer_order_sql)
        consumer_order_amount = self.cursor.fetchone()
        return consumer_order_amount[0]

    def get_consume_account(self, consumer_id):
        get_consumer_account_sql = "select ifnull(sum(value),0) from consumer_account_record where consumer_id = '%s' and expense_type = 1" % consumer_id
        self.cursor.execute(get_consumer_account_sql)
        consumer_account_amount = self.cursor.fetchone()
        return consumer_account_amount[0]

    def get_refund(self, consumer_id):
        get_refund_sql = "select ifnull(sum(value),0) from consumer_account_record where consumer_id = '%s' and expense_type IN (4, 5)" % consumer_id
        self.cursor.execute(get_refund_sql)
        refund = self.cursor.fetchone()
        return refund[0]

    def get_balance(self, consumer_id):
        get_balance_sql = "select ifnull(balance,0) from consumer_account where consumer_id = '%s'" % consumer_id
        self.cursor.execute(get_balance_sql)
        balance = self.cursor.fetchone()
        return balance[0]

    def confirm_consumer(self, consumer_id):
        charge_amount = self.get_charge(consumer_id)
        bind_amount = self.get_bind(consumer_id)
        refund = self.get_refund(consumer_id)
        consume_order_amount = self.get_consume_order(consumer_id)
        consume_account_amount = self.get_consume_account(consumer_id)
        balance = self.get_balance(consumer_id)
        left = charge_amount+bind_amount
        right = consume_order_amount + balance + refund
        if (left != right) \
                or (consume_order_amount != consume_account_amount):
            print "consumer_id = %s " % consumer_id
        print "chargeAmount: %s, ,bind_amount: %s ,consumeOrder: %s, accountAmount: %s, refund:%s, balance:%s, left:%s, right:%s " % \
                  (charge_amount, bind_amount, consume_order_amount, consume_account_amount, refund, balance, left, right)


    def file_source(self):
        fo = open("/Users/shengrui/acc.txt", "rw+")
        for index in range(406):
            line = fo.next()
            if index % 2 == 0:
                client = SimpleHttpClient.SimpleHttpClient()
                result = client.get("http://st.mwoperation.meiweishenghuo.com/2b/consumer/consumerRefund", {"consumerId":line[14:50]})
                print result.text

        fo.close()

    def main(self):
        get_consumer_sql = "select consumer_id from consumer_account where pay_password is not null"
        self.cursor.execute(get_consumer_sql)
        consumers = self.cursor.fetchall()
        for consumer in consumers:
            self.confirm_consumer(consumer[0])

account = ConfirmConsumerAccount()
account.confirm_consumer('ea8dbdb5-8c19-4e56-9cf6-e572ffc351a3')
account.confirm_consumer('e700dde3-1fe1-4e63-8781-9ab0ccf18040')



# consumer_id = e700dde3-1fe1-4e63-8781-9ab0ccf18040
# chargeAmount: 550, ,bind_amount: 0 ,consumeOrder: 551.67, accountAmount: 551.67, refund:0.01, balance:0.00, left:550, right:551.68
# consumer_id = ea8dbdb5-8c19-4e56-9cf6-e572ffc351a3
# chargeAmount: 550, ,bind_amount: 0 ,consumeOrder: 558.06, accountAmount: 558.06, refund:0.01, balance:0.00, left:550, right:558.07

# consumer_id = ea8dbdb5-8c19-4e56-9cf6-e572ffc351a3
# chargeAmount: 550, ,bind_amount: 0 ,consumeOrder: 558.06, accountAmount: 558.06, refund:0.01, balance:0.00, left:550, right:558.07
# consumer_id = e700dde3-1fe1-4e63-8781-9ab0ccf18040
# chargeAmount: 550, ,bind_amount: 0 ,consumeOrder: 551.67, accountAmount: 551.67, refund:0.00, balance:0.00, left:550, right:551.67
