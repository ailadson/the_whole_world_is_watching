import json
import datetime
import uuid
import base64
from google.appengine.api import app_identity
from baseHandler import BaseHandler

class FileUploadEndpointHandler(BaseHandler):
    def get(self):
        expires = '%sZ' % ((datetime.datetime.utcnow() + datetime.timedelta(hours=1)).isoformat()[:19])
        fname = 'uploads/%s.raw' % str(uuid.uuid4())
        policy = base64.b64encode(json.dumps({'expiration': expires,
                                             'conditions': [{'bucket': 'net_wwwatching'}, {'key': fname}]}))
        signed = base64.b64encode(app_identity.sign_blob(policy)[1])
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps({
            'method': 'POST', 'url': 'https://%s.commondatastorage.googleapis.com/' % 'net_wwwatching',
            'params' : {'key': fname, 'GoogleAccessId': app_identity.get_service_account_name(),
                       'signature': signed, 'policy': policy}
        }))