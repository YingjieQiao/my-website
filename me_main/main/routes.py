from flask import render_template, request, Blueprint
from me_main.models import Post

main = Blueprint('main', __name__)


@main.route('/home') # adding home page
def home():
    page = request.args.get("page", 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=3)
    return render_template("home.html", posts=posts)

@main.route('/') # pass in url using route
@main.route('/about') # adding about page
def about():
    return render_template("about.html", title="About")

