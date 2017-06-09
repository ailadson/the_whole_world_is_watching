from base_handler import BaseHandler
import webapp2

class MapHandler(BaseHandler):
    def get(self):
        city = self.request.headers.get('X-AppEngine-City')
        self.render('map', { 'city' : city })

app = webapp2.WSGIApplication([
    ('/', MapHandler),
], debug = True)
