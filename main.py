"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask, render_template
#from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)

#bootstrap = Bootstrap(app)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name = name)
	
if __name__ == '__main__':
	app.run(debug=True)
