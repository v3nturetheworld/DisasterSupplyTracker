from google.appengine.ext import db

class Post(db.Model):
	item = db.StringProperty(required = True)
	priority = db.StringProperty(required = True)
	location = db.StringProperty(required = True)
	donor = db.StringProperty(required = True)
	when = db.DateTimeProperty(auto_now_add = True)
	author = db.UserProperty(required = True)
