import os
from freelancehub import db
from freelancehub.services.forms import CheckoutForm
from freelancehub.models import Post, Service, User
from flask import render_template, request, Blueprint, flash, redirect, url_for
from flask_login import login_user, current_user, logout_user, login_required


services = Blueprint('services', __name__)


@services.route("/checkout/<int:post_id>", methods=['GET', 'POST'])
@login_required
def checkout(post_id):
    post = Post.query.get_or_404(post_id)
    form = CheckoutForm()
    form.price = post.price
    if request.method == "POST":
        if form.validate_on_submit():
            page = request.args.get('page', 1, type=int)
            user = User.query.filter_by(username=current_user.username).first_or_404()
            service = Service(post_id=post.id, buyer_id=user.id, buy_price=post.price)
            db.session.add(service)
            db.session.commit()
            flash('Your Purchase was successfull! Author of the Listing would contact you shortly on your Email Address', 'success')
            return redirect( url_for('users.history') )
    return render_template('service/checkout.html', title='Checkout',
                           post=post, form=form)
