from backend.response.requestHandler import RequestHandler
from importlib import resources
with resources.path('frontend.public', 'pages') as data_path:
    default_config_path = data_path

class PageHandler(RequestHandler):
    def __init__(self):
        super().__init__()
        self.content_type = 'text/html'

    def find(self, route_data):
        try:
            template_file = open('{}/{}'.format(default_config_path,route_data['pages']))
            self.contents = template_file
            self.setStatus(200)
            return True
        except:
            self.setStatus(404)
            return False