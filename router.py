from handlers.map import MapHandler
from handlers.search import SearchHandler
from handlers.upload import UploadHandler

import webapp2

app = webapp2.WSGIApplication([
    ('/', MapHandler),
    ('/search', SearchHandler),
    ('/upload', UploadHandler),
], debug = True)
