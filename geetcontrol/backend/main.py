import time
from http.server import HTTPServer
from backend.server import Server
# import server
from backend.qrdisp import QRDisplay

#Get IP address for computer on network

def main():
    qr = QRDisplay()
    qr.display()

    HOST_NAME = ''
    PORT_NUMBER = 8000

    httpd = HTTPServer((HOST_NAME, PORT_NUMBER), Server)
    print(time.asctime(), 'Server up - %s:%s' % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
    print(time.asctime(), 'Server down - %s:%s' % (HOST_NAME,PORT_NUMBER))

if __name__ == '__main__':
    main()
