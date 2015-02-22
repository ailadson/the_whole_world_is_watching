import jinja2
import os
from baseHandler import BaseHandler

jinja = jinja2.Environment(autoescape=True,
                           loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__))))


class MainPage(BaseHandler):
    def get(self):
        body_type = self.request.get('body')
        body_dict = {
            '': 'maps.html',
            'contrib': 'contrib.htm',
            'upload': 'upload.htm',
            'upload1': 'upload1.htm',
            'upload2': 'upload2.htm',
            'search': 'search.htm',
            'about': 'about.htm'
        }

        if self.request.get('search') == '1':
            body_values = {
                'cd': '',
                'results': self.session.get('results'),
                'choiceID': self.request.get('id')
            }
            print(self.session.get('results'))
        else:
            body_values = {
                'cd': '',
                'latlng': self.request.headers.get("X-AppEngine-CityLatLong")
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
