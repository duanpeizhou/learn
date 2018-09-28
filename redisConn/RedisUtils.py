# -*- coding: UTF-8 -*-
import redis


class RedisUtils:
    def __init__(self):
        pool = redis.ConnectionPool(host='172.17.29.197', port=6388, db=0, password='redis_mwlifer')
        self.redisPool = pool

    def get(self, key):
        redis_bar = redis.Redis(connection_pool=self.redisPool)
        return redis_bar.get(key)

    def execute_cmd(self, cmd):
        redis_bar = redis.Redis(connection_pool=self.redisPool)
        return redis_bar.execute_command(cmd)




