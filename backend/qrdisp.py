import socket
import pyqrcode
import png
from pyqrcode import QRCode

from PIL import Image


class QRDisplay:
    def __init__(self):
        #Find the IP of the computer
        self.ip = ''
        self.imgURL = 'temp.png'
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # doesn't even have to be reachable
            s.connect(('1.255.255.255', 1))
            self.ip = 'http://{0}:8000'.format(s.getsockname()[0])
        except:
            self.ip = ''
        finally:
            s.close()
        
        #Generate QR Code file
        url = pyqrcode.create(self.ip)
        url.png(self.imgURL, scale = 6)
    
    def display(self):
        img = Image.open(self.imgURL)
        img.show() 
                