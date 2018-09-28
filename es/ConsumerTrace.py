# -*- coding: UTF-8 -*-
import SimpleHttpClient
import json
import MySQLdb
import time

page_size = 1000


def get_data(traces):
    try:
        for t in traces:
            consumer_id = t['_id']
            items = t['_source']['consumerTraceItems']
            json_items = json.loads(items)
            for item in json_items:
                save_trace((consumer_id, time_tre(item['date']), item['vendorId']))
                # print "consumerId = %s , date = %d , vendorId = %s , coverId = %s " % (consumer_id, item['date'], item['vendorId'], item['coverId'])
    except KeyError:
        print "traces = %s " % traces


def pre_save(re):
    r = json.loads(re)
    scroll_id = r["_scroll_id"]
    print scroll_id
    result_len = len(r['hits']['hits'])
    hits = r['hits']
    if hits.has_key('hits'):
        get_data(hits['hits'])
    return scroll_id, result_len


def get_data_scroll():
    req = SimpleHttpClient.SimpleHttpClient()
    url = "http://39.106.168.8:9200/mwvendor_consumertrace/_search?scroll=1m"
    param = {"size": page_size}
    print param
    r = req.post(url, param)
    print r.text
    return pre_save(r.text)


def get_data_scroll_next(scroll_id):
    req = SimpleHttpClient.SimpleHttpClient()
    url = "http://39.106.168.8:9200/_search/scroll"
    print "get_data_scroll_next %s " % scroll_id
    param = {"scroll": "1m", "scroll_id": scroll_id}
    print param
    r = req.post(url, param)
    print r.text
    return pre_save(r.text)


db = MySQLdb.connect('47.95.232.160', 'root', 'pass123', 'test1', 3306, charset='utf8')
cursor = db.cursor()


def save_trace(item):
    insert_sql = "insert into consumer_trace(consumer_id,date,vendor_id) values ('%s','%s','%s')" % item
    # print insert_sql
    cursor.execute(insert_sql)


def time_tre(timeStamp):
    timeStamp = timeStamp / 1000
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime  # 2013--10--10 23:40:00


def main():
    times = 0
    scroll_id, result_len = get_data_scroll()
    while result_len == 3:
        scroll_id, result_len = get_data_scroll_next(scroll_id)
        db.commit()
        times = times + 1
        print times


main()
