#--coding:utf-8--

from http.server import BaseHTTPRequestHandler, HTTPServer
from os import path


class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
    # GET
    def do_GET(self):
        print(self.path)
        self.send_response(200, message="""{'a':1}""")
        self.send_header('Content-type', 'application/json')
        self.end_headers()


def run():
    port = 8000
    print('starting server, port', port)

    # Server settings
    server_address = ('localhost', port)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()