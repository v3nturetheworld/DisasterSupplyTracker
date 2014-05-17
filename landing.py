import webapp2
class main(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type']='text/plain'
		self.response.out.write("test")
app = webapp2.WSGIApplication([('/', main)], debug = True)