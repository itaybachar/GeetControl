from response.requestHandler import RequestHandler

class PageHandler(RequestHandler):
    def __init__(self):
        super().__init__()
        self.content_type = 'text/html'

    def find(self, route_data):
        try:
            template_file = open('../frontend/public/pages/{}'.format(route_data['pages']))
            self.contents = template_file
            self.setStatus(200)
            return True
        except:
            self.setStatus(404)
            return False