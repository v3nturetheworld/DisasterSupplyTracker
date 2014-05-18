from application import app
from models import Post
from decorators import login_required

from flask import render_template, flash, url_for, redirect
from flaskext import wtf
from flaskext.wtf import validators

from google.appengine.api import users

class PostForm(wtf.Form):
    item = wtf.StringField('item', validators=[validators.Required()])
    priority = wtf.StringField('priority', validators=[validators.Required()])
    location = wtf.StringField('location', validators=[validators.Required()])
    donor = wtf.StringField('donor', validators=[validators.Required()])

@app.route('/')
def redirect_to_home():
    return redirect(url_for('list_posts'))

@app.route('/posts')
def list_posts():
    posts = Post.all()
    return render_template('list_posts.html', posts=posts)

@app.route('/posts/new', methods = ['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(item = form.item.data,
        			priority = form.priority.data,
        			location = form.location.data,
                    donor = form.donor.data,
                    author = users.get_current_user())
        post.put()
        flash('Post saved on database.')
        return redirect(url_for('list_posts'))
    return render_template('new_post.html', form=form)