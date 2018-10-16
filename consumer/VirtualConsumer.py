# -*- coding: UTF-8 -*-

import json
import socket
from multiprocessing import Process

from mysql.online import MySQL
from mysql.test import MySQL as TestMysql

db = MySQL()
test_db = TestMysql("mwpt")
page_size = 60


def get_virtual_number():
    sql = "select count(id) from consumer where is_true = 0"
    rows = test_db.get_data_by_sql(sql)
    print int(rows[0][0])
    return int(rows[0][0])


def handle_client(client_socket):
    """
    处理客户端请求
    """
    request_data = client_socket.recv(1024)
    # 构造响应数据
    response_start_line = "HTTP/1.1 200 OK\r\n"
    response_headers = "Access-Control-Allow-Origin:*\r\n"

    is_get_amount = request_data.find("getAmount")
    if is_get_amount >= 0:
        amount = get_virtual_number()
        result = {"amount": amount}
        r = response_start_line + response_headers + "\r\n" + json.dumps(result)+ "\r\n"
        content = bytes(r)
        client_socket.send(content)
        client_socket.close()
        return
    begin = request_data.find("/?") + 2
    end = request_data.find(" HTTP/1.1")
    param = request_data[begin:end]
    p = param.split("=")
    page_no = 1;
    if p[0] == "pageNo":
        page_no = int(p[1])

    start = (page_no - 1) * page_size


    consumers = []
    sql = "select nick_name,head_img_url from consumer where nick_name is not null limit %d , %d;" % (start, page_size)
    rows = db.get_data_by_sql(sql)
    for row in rows:
        consumer = {"nickName": row[0], "headImgUrl": row[1]}
        consumers.append(consumer)

    # response_body = "<h1>Python HTTP 端 Test</h1>"
    response_body = json.dumps(consumers)
    response = response_start_line + response_headers + "\r\n" + response_body

    # 向客户端返回响应数据
    content = bytes(response);
    client_socket.send(content)

    # 关闭客户端连接
    client_socket.close()





if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("", 8000))
    server_socket.listen(128)

    while True:
        client_socket, client_address = server_socket.accept()
        print("[%s, %s]用户连接上了" % client_address)
        handle_client_process = Process(target=handle_client, args=(client_socket,))
        handle_client_process.start()
        client_socket.close()