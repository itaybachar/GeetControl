import os

from http.server import BaseHTTPRequestHandler
from routes.main import routes, post_routes
from response.pageHandler import PageHandler
from response.badRequestHandler import BadRequestHandler
from response.staticHandler import StaticHandler
from response.actionHandler import InfoHandler, RemoteControlHandler

import json

class Server(BaseHTTPRequestHandler):
    def do_HEAD(self):
        return
    def do_POST(self):
        if self.path in post_routes:
            post_data = json.loads(self.rfile.read(int(self.headers['Content-Length'])).decode("utf-8"))
            # print("GOT POST: " + json.dumps(post_data))

            if post_data.get('op',None) == 'remote':
                remote_data = post_data.get('data',None)
                if remote_data is None:
                    handler = BadRequestHandler()
                else:
                    handler = RemoteControlHandler()
                    handler.writeAction(remote_data)    
            else: 
                handler = BadRequestHandler()
        else:
            handler = BadRequestHandler()

        self.respond({
            'handler': handler 
        })

    def do_GET(self):
   
        split_path = os.path.splitext(self.path)
        req_extension = split_path[1]

        if req_extension is "" or req_extension is ".html":
            if self.path in routes:
                handler = PageHandler()
                handler.find(routes[self.path])
            elif self.path in ("/info",):
                handler = InfoHandler()
            else:
                handler = BadRequestHandler()
        elif req_extension is ".py":
            handler = BadRequestHandler()
        else:
            handler = StaticHandler()
            handler.find(self.path)
        
        self.respond({
            'handler': handler 
        })

    def handle_http(self, handler):
        status_code = handler.getStatus()

        self.send_response(status_code)

        if status_code is 200:
            content = handler.getContents()
            self.send_header('Content-type',handler.getContentType())
        else:
            content = "404 Not Found"
        
        self.end_headers()

        if isinstance(content, (bytes, bytearray)):
            return content
            
        return bytes(content,"UTF-8")

    def respond(self, opts):
        content = self.handle_http(opts['handler'])
        self.wfile.write(content)

    def log_message(self, format, *args):
        return