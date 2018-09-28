# -*- coding: UTF-8 -*-
import SimpleHttpClient

req = SimpleHttpClient.SimpleHttpClient('9e2402ba-6703-11e7-a5fa-9801a79f70e5_e4bdb66c735b4ca4bd397f3de877b645')


def refund(order_id):
    r = req.get("http://st.mwoperation.meiweishenghuo.com/api/probe/orderRefund", {"orderId": order_id})
    print "orderId = %s, result = %s" % (order_id, r.text)


def compensate(consumer_id, value):
    r = req.get("http://st.mwoperation.meiweishenghuo.com/api/probe/increaseBalance", {"consumerId": consumer_id, "value":value})
    print "consumerId = %s, value = %f, result = %s" % (consumer_id, value, r.text)








