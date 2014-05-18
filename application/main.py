from flask import Flask, render_template
"""`main` is the top level module for your Flask application."""

app = Flask(__name__)

#bootstrap = Bootstrap(app)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

#manager = Manager(app)
#bootstrap = Bootstrap(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name = name)
	
if __name__ == '__main__':
	app.run(debug=True)
