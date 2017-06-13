import webapp2
import os
import jinja2

JINJA = jinja2.Environment(
            loader=jinja2.FileSystemLoader(
                '{0}/..'.format(os.path.dirname(__file__))) ,
            extensions=['jinja2.ext.autoescape'],
            autoescape=True)

class BaseHandler(webapp2.RequestHandler):
    def render(self, filename, context):
        app_file = 'views/app.html'.format()
        app = JINJA.get_template(app_file)

        template_file = 'views/{0}.html'.format(filename)
        context['filename'] = template_file
        context['page'] = filename

        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(app.render(context))
