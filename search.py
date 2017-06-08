import webapp2
from base_handler import BaseHandler

class MapHandler(BaseHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello World!')

app = webapp2.WSGIApplication([
    ('/', MapHandler),
], debug = True)
