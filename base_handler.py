import webapp2
import os
import jinja2

JINJA = jinja2.Environment(
            loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
            extensions=['jinja2.ext.autoescape'],
            autoescape=True)

class BaseHandler(webapp2.RequestHandler):
    def render(self, filename, context):
        self.response.headers['Content-Type'] = 'text/html'
        app = JINJA.get_template('views/app.html')
        template_file = 'views/{0}.html'.format(filename)

        context['filename'] = template_file
        context['page'] = filename

        self.response.write(app.render(context))
