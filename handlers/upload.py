from base_handler import BaseHandler
from keys import MAPS_API_KEY
import datetime
import dateutil.parser
import tasks

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
        if input_type == 'vidfile':
            Incident.create(
                cloud_id=self.request.params.get('incident[cloud_id]'),
                uploader_ip=self.request.remote_addr)
        elif input_type == 'required' or input_type == 'optional':
            data = Incident.format_data(self.request.params)
            incident = Incident.update_from_form(
                self.request.params.get('incident[cloud_id]'), data)
            incident.encode_video()
        self.response.write(input_type)
