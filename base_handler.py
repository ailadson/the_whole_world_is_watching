import webapp2
import os
import jinja2

JINJA = jinja2.Environment(
            loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
            extensions=['jinja2.ext.autoescape'],
            autoescape=True)

API_KEY = "AIzaSyC1kGoXOh-Hc32V_rJSt1ILQ_UH5y5KoLU"

class BaseHandler(webapp2.RequestHandler):
    def render(self, filename, context):
        app = JINJA.get_template('views/app.html')
        template_file = 'views/{0}.html'.format(filename)


        self.response.write(
            app.render({ 'filename' : template_file, 'API_KEY' : API_KEY }))
