import jinja2
import os
from baseHandler import BaseHandler
from uploadHandler import UploadFormHandler1, UploadFormHandler2 

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
            print(self.session.get('results'))
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
