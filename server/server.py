from http.server import BaseHTTPRequestHandler, HTTPServer
import datetime
log = open('./log/log.txt', 'w')
log.write(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S") + " server started\n")
log.close()
class S(BaseHTTPRequestHandler):
   
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        log = open('./log/log.txt', 'a')
        log.write(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S") + " get: " + self.path + "\n")
        if str(self.path)=='/?ping':
            self._set_response()
            self.wfile.write("pong".encode())
            log.write(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S") + " send: pong\n")
        else:
            self._set_response()
            self.wfile.write("what?!".encode())
            log.write(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S") + " send: what?!\n")
        log.close()   
if __name__ == '__main__':
    
    
    
    webServer = HTTPServer(('',8080 ),S)

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    log = open('./log/log.txt', 'a')
    log.write(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S") + " server stopped \n")
    log.close()
    webServer.server_close()
    
    
