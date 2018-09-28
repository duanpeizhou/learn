# -*- coding: UTF-8 -*-
import json


def main():
    f = open("/Users/shengrui/refund.txt", 'r')

    s = " "
    line = 0
    balance = 0
    refund = 0
    while len(s) > 0:
        s = f.readline()
        if line % 2 == 0 and len(s) > 48:
            j = s[48:]
            print(j)
            js = json.loads(j)
            balance += js['data']['items'][0]['balance']
            refund += js['data']['items'][0]['refund']
            print "balance = %f, refund = %f" % (balance, refund)
        line += 1

    print line
    print "balance = %f, refund = %f" % (balance,refund)
main()
# 141247.72  667.96   140579.76
# 105132.95  462.09   104670.86