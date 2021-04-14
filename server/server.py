from http.server import BaseHTTPRequestHandler, HTTPServer

class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_response()
        self.wfile.write("pong".encode())

#def run(server_class=HTTPServer, handler_class=S, port=8080):
#    server_address = ('', port)
#    httpd = server_class(server_address, handler_class)
#    try:
#        httpd.serve_forever()
#    except KeyboardInterrupt:
#        pass
#    httpd.server_close()

if __name__ == '__main__':
    webServer = HTTPServer(('',8080 ),S)

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
