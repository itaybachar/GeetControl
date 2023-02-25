import socket 
import json
import io

from backend.response.requestHandler import RequestHandler
from backend.controller.remoteController import ControllerManager

class InfoHandler(RequestHandler):
    def __init__(self):
        super().__init__()
        self.content_type = 'application/json'
        self.setStatus(200)

        # Get IP and set contents
        self.getIP()
        self.contents.setData(json.dumps({"ip": self.ip}))

    def getIP(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # doesn't even have to be reachable
            s.connect(('1.255.255.255', 1))
            self.ip = s.getsockname()[0]
        except:
            self.ip = ""
        finally:
            s.close()

class RemoteControlHandler(RequestHandler):
    def __init__(self):
        super().__init__()
        self.content_type = 'text/plain'
        self.setStatus(200)
        self.contents.setData("success")

        self.controller_manager = ControllerManager()
    
    def writeAction(self, action):
        self.controller_manager.add(action)
