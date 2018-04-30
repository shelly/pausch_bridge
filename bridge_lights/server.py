import SocketServer
from BaseHTTPServer import BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get received!")

        self.send_response(200)

httpd = SocketServer.TCPServer(("", 8080), MyHandler)
httpd.serve_forever()
