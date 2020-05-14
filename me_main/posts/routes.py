from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from me_main import db
from me_main.models import Post, Comment
from me_main.posts.forms import PostForm, CommentForm


posts = Blueprint('posts', __name__)


@posts.route('/post/new', methods=["GET", "POST"]) # create a new post
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash("Post created lololol", "success")
        return redirect(url_for("main.home"))
    return render_template("create_post.html", title="New Post",
                           form=form, legend='New Post')

@posts.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id):
    post = Post.query.get_or_404(post_id)
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(content=form.content.data, post=post,
                          author=current_user._get_current_object())
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been published', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    comments = post.comments
    print(type(comments))
    return render_template("post.html", title=post.title, post=post,
                           comments=comments, form=form)
    #return render_template("post.html", title=post.title, post=post)


@posts.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash("Your post has been updated.", "success")
        return redirect(url_for("posts.post", post_id=post.id))
    elif request.method == "GET":
        form.title.data = post.title
        form.content.data = post.content
    return render_template("create_post.html", title="Update Post",
                           form=form, legend='Update Post')


@posts.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post.comments)
    db.session.delete(post)
    db.session.commit()
    flash("Your post has been deleted.", "success")
    return redirect(url_for('main.home'))

