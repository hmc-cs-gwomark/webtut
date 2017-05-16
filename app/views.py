from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Miguel'} #fake user
	posts = [
		{
			'author': {'username': 'weirdo'},
			'body': 'noice',
			'date': "07-06-2017" 
		},
		{
			'author': {'username': 'nancy'},
			'body': 'sgo boys',
			'date': "07-09-2017" 
		}
	]
	return render_template('index.html', title='Home', user=user, posts=posts)