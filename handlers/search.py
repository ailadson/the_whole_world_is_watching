from base_handler import BaseHandler

class SearchHandler(BaseHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello World!')
