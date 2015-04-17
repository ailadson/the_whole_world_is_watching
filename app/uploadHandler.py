import jinja2
import os
import json
import helpers
import cloudstorage
import tasks

from baseHandler import BaseHandler
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers

jinja = jinja2.Environment(autoescape=True,
                           loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__))))


class UploadFormHandler(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        postData = self.request.get
        f = postData('file')
        locData = helpers.createLocData(postData('lat'), postData('lng'))
        record = helpers.createRecord(postData,locData,f)
        tasks.create(record)
        
class UploadFormHandler2(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        file_info = self.get_file_infos()[0]
        filename = file_info.gs_object_name.split("net_wwwatching/raw/")[1]
        type = file_info.content_type.split("/")[1]
        postData = self.request.get
        locData = createLocData(postData('lat'), postData('lng'))
        record = helpers.createRecord(postData,locData,filename)
        
        