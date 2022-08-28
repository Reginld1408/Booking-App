from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html", user=current_user)


@views.route('/book')
@login_required
def book():
    return render_template("book.html")


@views.route('/mybookings')
@login_required
def mybookings():
    return render_template("mybookings.html")


