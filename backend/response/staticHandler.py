import os

from response.requestHandler import RequestHandler

class StaticHandler(RequestHandler):
    def __init__(self):
        self.filetypes = {
            ".js": "text/javascript",
            ".css": "text/css",
            ".jpg": "text/jpg",
            ".jpeg": "text/jpeg",
            ".png": "text/png",
        }

    def find(self, file_path):
        split_path = os.path.splitext(file_path)
        extension = split_path[1]

        try:
            if ".." in file_path:
                raise Exception("Bad URL")
            
            if extension in (".jpg", ".jpeg", ".png"):
                self.contents = open("../frontend/public{}".format(file_path), 'rb')
            else:
                self.contents = open("../frontend/public{}".format(file_path), 'r')
            
            self.setContentType(extension)
            self.setStatus(200)
            return True
        except:
            self.setContentType('notfound')
            self.setStatus(404)
            return False
    
    def setContentType(self, ext):
        self.content_type = self.filetypes.get(ext,"notfound")

