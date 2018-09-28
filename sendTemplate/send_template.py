# -*- coding: UTF-8 -*-
import SimpleHttpClient
from mysql.online import MySQL

req = SimpleHttpClient.SimpleHttpClient("9e2402ba-6703-11e7-a5fa-9801a79f70e5_cdde1eae-479b-4dc4-a2f0-2a3a492bf042")
db = MySQL()



message_start_server = {
    "touser": "oksD41JrSf_LbzCAmLk7glMvN_yY",
    "template_id": "el85tO91yRmWpgiT1pRuJNmAZg3u4kY8LG2FvzJDFLA",
    "url": "https://ttmwsh.meiweishenghuo.com/weixin/?fr=mp_template_lottery#/v-draw-lottery",
    "data": {
        "first": {
            "value": "你！没！有！看！错！\n每日抽奖活动继续造势\n会员！红包！100%中奖\n每天均可参与免费抽奖！！！\n每天均可参与免费抽奖！！！\n每天均可参与免费抽奖！！！",
            "color": "#173177"
        },
        "keyword1": {
            "value": "每日抽奖活动",
            "color": "#000000"
        },
        "keyword2": {
            "value": "即日起",
            "color": "#000000"
        }
        ,
        "remark":{
            "value": "点击进入抽奖活动页面>>",
            "color": "#173177"
        }
    }
}


message_bind = {
    "touser": "oksD41JrSf_LbzCAmLk7glMvN_yY",
    "template_id": "IpiIUi33ZZ3xIzbersAuqDcv6eOb6iFwfsBZLhsPuDg",
    "url": "https://ttmwsh.meiweishenghuo.com/weixin/?fr=mp_template#/",
    "data": {
        "first": {
            "value": "你的“5元”红包即将过期了，快去使用吧~",
            "color": "#173177"
        },
        "keyword1": {
            "value": "客官",
            "color": "#173177"
        },
        "keyword2": {
            "value": "美食是可以吃下去的幸福回忆，忙碌了一天，订份餐好好犒劳犒劳自己吧，还能提前预定哦~",
            "color": "#173177"
        }
        # ,
        # "remark":{
        #     "value": "\n恢复运营时间暂未确定，敬请关注公众号等待通知。若您有其他疑问，可通过公众号、客服电话进行咨询，再次感谢您的支持和理解——美味生活机哥。",
        #     "color": "#173177"
        # }
    }
}

send_coupon = {
    "touser": "oksD41JrSf_LbzCAmLk7glMvN_yY",
    "template_id": "ACPfikvL1fEtlo4vH4702ZQ0THS3vHolhb8OpU2D2TY",
    "url": "https://ttmwsh.meiweishenghuo.com/weixin/?fr=mp_template#/",
    "data": {
        "result": {
            "value": "天降红包来袭～\n恭喜你被“5元购餐红包”砸中，赶快犒劳一下辛苦奋斗的自己吧～",
            "color": "#173177"
        },
        "withdrawMoney": {
            "value": "5元购餐红包",
            "color": "#000000"
        },
        "withdrawTime": {
            "value": "仅限今日现购正餐可用",
            "color": "#000000"
        },
        "cardInfo": {
            "value": "天降红包",
            "color": "#000000"
        },
        "arrivedTime": {
            "value": "红包列表",
            "color": "#000000"
        },
        "remark":{
            "value": "\n点击进入订餐页面>>",
            "color": "#173177"
        }
    }
}

def execute_start_message(message, open_id):
    message["touser"] = open_id
    print(message)
    r = req.post("http://mwtoc.meiweishenghuo.com/api/probe/sendTemplateMessage", message)
    print(r.text)


def send():
    sql = """"""
    rows = db.get_data_by_sql(sql)
    for open_id in rows:
        execute_start_message(send_coupon, open_id[0])


execute_start_message(send_coupon, "ouLfS1Ix-Tnhn5thzJGeq2221_Jc")


