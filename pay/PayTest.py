# -*- coding: UTF-8 -*-
import SimpleHttpClient
import json

req = SimpleHttpClient.SimpleHttpClient("oFTYt0gRYE5riSprWOq8cIO6vp7M")

coupon_id = "06f99e11-9419-4507-b5cd-790c7925c9c7"
confirm_pay_url = "http://127.0.0.1:8080/ttmwsh/order/confirmPay"
vendor_id = "10e059ea-a09d-4ebe-a4b3-2dcfd1f06d77"


def vendor_goods_wx_normal_confirm_pay(group_id):
    param = {
        "groups": [{
            "goodsGroupId": group_id,
            "amount": 1
        }],
        "vendorId": vendor_id,
        "buyType": 1,
        "isPack": 0,
        "couponId": coupon_id,
        "orderType": 1,
        "tradeType": 1
    }
    result = req.post(confirm_pay_url, param)
    print "vendor_goods_wx_normal_confirm_pay = %s" % json.dumps(json.loads(result.text), indent=1)


def vendor_goods_wx_reserve_confirm_pay(group_id):
    param = {
        "groups": [{
            "goodsGroupId": group_id,
            "amount": 1
        }],
        "vendorId": vendor_id,
        "buyType": 2,
        "isPack": 0,
        "couponId": coupon_id,
        "reserveDateStr": "2018-03-12",
        "orderType": 1,
        "tradeType": 1
    }
    result = req.post(confirm_pay_url, param)
    print "vendor_goods_wx_reserve_confirm_pay = %s" % json.dumps(json.loads(result.text), indent=1)


def vendor_goods_account_normal_confirm_pay(group_id):
    param = {
        "groups": [{
            "goodsGroupId": group_id,
            "amount": 1
        }],
        "vendorId": vendor_id,
        "buyType": 1,
        "isPack": 0,
        "couponId": coupon_id,
        "orderType": 1,
        "tradeType": 4
    }
    result = req.post(confirm_pay_url, param)
    print "vendor_goods_account_normal_confirm_pay = %s" % json.dumps(json.loads(result.text), indent=1)


def vendor_goods_account_reserve_confirm_pay(group_id):
    param = {
        "groups": [{
            "goodsGroupId": group_id,
            "amount": 1
        }],
        "vendorId": vendor_id,
        "buyType": 2,
        "isPack": 0,
        "couponId": coupon_id,
        "reserveDateStr": "2018-03-12",
        "orderType": 1,
        "tradeType": 4
    }
    result = req.post(confirm_pay_url, param)
    print "vendor_goods_account_reserve_confirm_pay = %s" % json.dumps(json.loads(result.text), indent=1)


def vendor_recharge_normal_confirm_pay():
    param = {
        "vendorId": vendor_id,
        "buyType": 1,
        "isPack": 0,
        "orderType": 2,
        "tradeType": 1,
        "payAmount": 90
    }
    result = req.post(confirm_pay_url, param)
    print "vendor_recharge_normal_confirm_pay = %s" % json.dumps(json.loads(result.text), indent=1)


group_id = "77599dab-a547-4810-b089-9c584a5e6fd5"
# vendor_goods_wx_normal_confirm_pay(group_id)
# vendor_goods_wx_reserve_confirm_pay(group_id)
# vendor_goods_account_normal_confirm_pay(group_id)
# vendor_goods_account_reserve_confirm_pay(group_id)
vendor_recharge_normal_confirm_pay()
