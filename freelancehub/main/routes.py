from flask import render_template, request, Blueprint
from freelancehub.models import Post
import os


main = Blueprint('main', __name__)


if os.path.isfile('/etc/freelancehub_about.txt'):
    about_path = '/etc/freelancehub_about.txt'
else:
    script_dir = os.path.dirname(__file__)
    rel_path = '../freelancehub_about.txt'
    about_path = os.path.join(script_dir, rel_path)
with open(about_path) as f:
    about_list = [line for line in f.readlines()]


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query\
        .filter_by(listed=1)\
        .order_by(Post.date_posted.desc()).paginate(page=page, per_page=12)
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About', created_by=about_list)
