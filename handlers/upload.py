from base_handler import BaseHandler
from keys import MAPS_API_KEY

from cloud_storage.storage import get_signed_url_upload_endpoint
from datastore.incident import Incident

class UploadHandler(BaseHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.render('upload', {
            'MAPS_API_KEY' : MAPS_API_KEY,
            'file_upload_endpoint' : get_signed_url_upload_endpoint() })

    def post(self):
        input_type = self.request.params.get('input_type')
        print(input_type)
        if input_type == 'vidfile':
            print('-----------------------------')
            incident = Incident(
                cloud_id=self.request.params.get('incident[cloud_id]'),
                upload_ip=self.request.remote_addr)
            incident.put()
        self.response.write('hey')
        # Incident(
        #     #required location
        #     lat=ndb.FloatProperty(),
        #     lng=ndb.FloatProperty(),
        #     country=ndb.StringProperty(),
        #     state=ndb.StringProperty(),
        #     city_state=ndb.StringProperty(),
        #     city=ndb.StringProperty(),
        #     neighborhood=ndb.StringProperty(),
        #     zipCode=ndb.StringProperty(),
        #
        #     #incident data
        #     about=ndb.TextProperty(indexe=alse),
        #     brutal=ndb.BooleanProperty(),
        #     fatal=ndb.BooleanProperty(),
        #     docile=ndb.BooleanProperty(),
        #
        #     #stage
        #     has_encoded=ndb.BooleanProperty(),
        #     has_required_data=ndb.BooleanProperty(),
        #     has_optional_data=ndb.BooleanProperty(),
        #
        #     #meta data
        #     promoted=ndb.IntegerProperty(),
        #     views=ndb.IntegerProperty(),
        #     flagged=ndb.BooleanProperty(),
        #     flagReason=ndb.StringProperty())
