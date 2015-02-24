import jinja2
import os
import json
import helpers

from baseHandler import BaseHandler
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers

jinja = jinja2.Environment(autoescape=True,
                           loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__))))

class UploadFormHandler1(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        body_values = {
            'date' : self.request.get('date'),
            'brutal' : self.request.get('brutal'),
            'fatal' : self.request.get('fatal'),
            'lat' : self.request.get('lat'),
            'lng' : self.request.get('lng'),
            'upload_url' : blobstore.create_upload_url('/upload2' ,gs_bucket_name='net_wwwatching/raw')
        }
                
        top = jinja.get_template('html/top.html')
        head = jinja.get_template('html/head.html')
        header=jinja.get_template('html/navBar.html')
        body = jinja.get_template('html/upload1.html')
        bottom = jinja.get_template('html/bottom.html')
        
        self.response.write(top.render())
        self.response.write(head.render({'bt': 'upload'}))
        self.response.write(header.render())
        self.response.write(body.render(body_values))
        self.response.write(bottom.render())
        
class UploadFormHandler2(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        file_info = self.get_file_infos()[0]
        filename = file_info.gs_object_name.split("net_wwwatching/raw/")[1]
        type = file_info.content_type.split("/")[1]
        postData = self.request.get
        locData = helpers.createLocData(postData)
        record = helpers.createRecord(postData,locData,filename,type)