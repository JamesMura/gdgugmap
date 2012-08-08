#!/usr/bin/env python
from google.appengine.ext.webapp import template
import webapp2
import os
class GDGRequestHandler(webapp2.RequestHandler):
	def render(self, name, **data):
		if not data:
			data = {}
		path = os.path.join(os.path.dirname(__file__), 'templates/')
		self.response.out.write(template.render(path+name+".html", data))
class MainHandler(GDGRequestHandler):
    def get(self):
        self.render('index')

app = webapp2.WSGIApplication([('/', MainHandler)],
                              debug=True)
