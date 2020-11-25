from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from freelancehub import db
from freelancehub.models import Post
from freelancehub.posts.forms import PostForm
from freelancehub.posts.utils import save_picture

posts = Blueprint('posts', __name__)


@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            post = Post(title=form.title.data, content=form.content.data,
                        author=current_user, image_file=picture_file, price=form.price.data)
        else:
            post = Post(title=form.title.data, content=form.content.data,
                        author=current_user, price=form.price.data)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post',
                           form=form, legend='New Post')


@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            post.image_file = picture_file
        post.price = form.price.data
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        form.image_file = post.image_file
        form.price.data = post.price
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')


@posts.route("/post/<int:post_id>/unlist", methods=['POST'])
@login_required
def unlist_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    post.listed = 0
    # db.session.delete(post)
    db.session.commit()
    flash('Your post has been Unlisted!', 'success')
    return redirect(url_for('main.home'))


@posts.route("/post/<int:post_id>/relist", methods=['POST'])
@login_required
def relist_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    post.listed = 1
    # db.session.delete(post)
    db.session.commit()
    flash('Your post has been Relisted!', 'success')
    return redirect(url_for('main.home'))
