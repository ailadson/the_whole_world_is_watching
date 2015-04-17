import jinja2
import os
from baseHandler import BaseHandler
from uploadHandler import UploadFormHandler, UploadFormHandler2
from fileUploadHandler import FileUploadEndpointHandler
from encoderHandler import EncoderHandler
import helpers
import tasks


DEV_MODE = True

jinja = jinja2.Environment(autoescape=True,
                           loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__))))


class MainPage(BaseHandler):
    def get(self):
        body_type = self.request.get('body')
        body_dict = {
            '': 'maps.html',
            'vid' : 'video.html',
            'contrib': 'contribute.html',
            'upload': 'upload.html',
            'search': 'search.htm',
            'about': 'about.html'
        }

        if self.request.get('search') == '1':
            body_values = {
                'cd': '',
                'results': self.session.get('results'),
                'choiceID': self.request.get('id'),
                'dev_mode' : DEV_MODE
            }
           
        else:
            body_values = {
                'cd': '',
                'latlng': self.request.headers.get("X-AppEngine-CityLatLong"),
                'dev_mode' : DEV_MODE
            }

        top = jinja.get_template('html/top.html')
        head = jinja.get_template('html/head.html')
        navBar = jinja.get_template('html/navBar.html')
        body = jinja.get_template('html/'+body_dict[body_type])
        bottom = jinja.get_template('html/bottom.html')

        self.response.write(top.render())
        self.response.write(head.render({'bt': body_type}))
        self.response.write(navBar.render())
        self.response.write(body.render(body_values))
        self.response.write(bottom.render())
        

class QuickRecord(BaseHandler):
    def get(self):
        top = jinja.get_template('html/top.html')
        head = jinja.get_template('html/head.html')

        body = jinja.get_template('html/r.html')
        bottom = jinja.get_template('html/bottom.html')

        self.response.write(top.render())
        self.response.write(head.render({'bt': 'r'}))
        self.response.write(body.render())
        self.response.write(bottom.render())
        
    def post(self):
        f = self.request.get("file")
        
        #get location or set some default
        if self.request.headers.get("X-AppEngine-CityLatLong") is not None:
            latlng = self.request.headers.get("X-AppEngine-CityLatLong").split(',')
        else:
            latlng = ['41.878114','-87.629798'] #FOR DEV PURPOSES!! CHANGE
            
        locData = helpers.createLocData(latlng[0],latlng[1])
        record = helpers.createRecord(self.request.get,locData,f)
        tasks.create(record)
        id = record.id
#        self.response.write(latlng)
        top = jinja.get_template('html/top.html')
        head = jinja.get_template('html/head.html')
        navBar = jinja.get_template('html/navBar.html')
        body = jinja.get_template('html/r_thankyou.html')
        bottom = jinja.get_template('html/bottom.html')
        
        self.response.write(top.render())
        self.response.write(head.render({'bt': 'r'}))
        self.response.write(navBar.render())
        self.response.write(body.render({'id': id}))
        self.response.write(bottom.render())
        