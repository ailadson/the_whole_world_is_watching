from base_handler import BaseHandler
from keys import MAPS_API_KEY

class MapHandler(BaseHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        city = self.request.headers.get('X-AppEngine-City')
        self.render('map', { 'city' : city, 'MAPS_API_KEY' : MAPS_API_KEY })