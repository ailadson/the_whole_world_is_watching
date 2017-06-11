import webapp2
from base_handler import BaseHandler
from keys import MAPS_API_KEY

class UploadHandler(BaseHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.render('upload', { 'MAPS_API_KEY' : MAPS_API_KEY })

    def post(self):
        pass

app = webapp2.WSGIApplication([
    ('/upload', UploadHandler),
], debug = True)
