import time
from http.server import HTTPServer
from server import Server
from qrdisp import QRDisplay

qr = QRDisplay()
qr.display()

#Get IP address for computer on network

HOST_NAME = ''
PORT_NUMBER = 8000

if __name__ == '__main__':
    httpd = HTTPServer((HOST_NAME, PORT_NUMBER), Server)
    print(time.asctime(), 'Server up - %s:%s' % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
    print(time.asctime(), 'Server down - %s:%s' % (HOST_NAME,PORT_NUMBER))
