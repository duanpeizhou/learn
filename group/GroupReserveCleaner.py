# -*- coding: UTF-8 -*-

import redisConn.RedisUtils
import SimpleHttpClient
import threading

# print sys.path


class GroupReserveCleaner:

    def __init__(self):
        self.redis_util = redisConn.RedisUtils.RedisUtils()
        self.req = SimpleHttpClient.SimpleHttpClient()
        self.cover_group_url = "http://mwtoc.meiweishenghuo.com/api/probe/clearCoverGroupReserve"
        self.cover_url = "http://mwtoc.meiweishenghuo.com/api/probe/clearCoverReserve"

    def clean_cover_group_reserve(self, date):
        keys = self.redis_util.execute_cmd("keys vendor_group_count_*_"+date)
        for key in keys:
            p = {"oldKey": key}
            result = self.req.get(self.cover_group_url, param=p)
            print result.text

    def clean_cover_reserve(self, date):
        keys = self.redis_util.execute_cmd("keys vendor_left_reserve_amount_*_"+date)
        for key in keys:
            p = {"oldKey": key}
            result = self.req.get(self.cover_url, param=p)
            print result.text

    def execute_clean(self):
        date_list = ["2017-12-05", "2017-12-06", "2017-12-07", "2017-12-08"]
        for date in date_list:
            threading.Thread(target=self.clean_cover_group_reserve(date)).start()
            threading.Thread(target=self.clean_cover_reserve(date)).start()

    def test(self):
        print "sssss"

