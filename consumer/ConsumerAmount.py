# -*- coding: UTF-8 -*-

from datetime import date
from datetime import timedelta
import SimpleHttpClient


begin_date = date(2018, 1, 22)

one_day = timedelta(days=1)
client = SimpleHttpClient.SimpleHttpClient()

while begin_date < date.today():
    begin_date = begin_date+one_day
    print begin_date
    r = client.get("http://test.mwoperation.meiweishenghuo.com/api/probe/clearConsumerAmount", {"localDate": begin_date})
    print r.text



