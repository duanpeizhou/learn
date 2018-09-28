# -*- coding: UTF-8 -*-

import requests
import urllib
import json

class SimpleHttpClient:
    def __init__(self, p):
        self.header = {
            "Content-Type": "application/json; charset=utf-8",
            "Referer": "http://st.mwoperation.meiweishenghuo.com/",
            "vendor-auth-ssid": p,
            "ttmwsh-open-id": p
        }

    def get(self, url, param):
        r = requests.get(url=url, params=urllib.urlencode(param), headers=self.header)
        # print r.url
        return r

    def post(self, url, param):
        r = requests.post(url=url, data=json.dumps(param), headers=self.header)
        return r
