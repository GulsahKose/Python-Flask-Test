from flask import Flask,abort, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
	#return 'Index!'
	return redirect(url_for('hello'))

@app.route('/hello')
def hello():
	#return 'Hello'
	abort(302)

@app.route('/user/<username>')
def show_user_profile(username):
	# show the user profile for that user
	return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
	# show the post with the given id, the id is an integer
	return 'Post %d' % post_id

@app.route('/projects/')
def projects():
	return 'The project page'

@app.route('/about')
def about():
	return 'The about page'

if __name__ == '__main__':
	app.run()
