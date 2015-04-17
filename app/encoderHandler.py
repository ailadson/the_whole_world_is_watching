import tasks
from datastore import Record

from baseHandler import BaseHandler

class EncoderHandler(BaseHandler):
    def get(self):
        key = self.request.get('key')
        id = self.request.get('id')
        
        if key == tasks.AUTH_CODE:
            q = Record.all()
            q.filter("id =", id)
            vidRecord = q.get()
            vidRecord.encoded = True
            vidRecord.put()
        else:
            self.abort(404)