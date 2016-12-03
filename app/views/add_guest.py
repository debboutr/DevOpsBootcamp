from flask import flash, redirect, render_template, url_for
from sqlalchemy.exc import IntegrityError

from app import app, db
from app.forms import AddGuestForm
from app.models import Guest
from app.util import flash_form_errors


# TODO: Add the proper methods for this route, then have this function render a
#       template containing the AddGuestForm and handle form submissions
@app.route('/guests/create', methods=["GET", "POST"])
def add_guest():
    """
    """
    form = AddGuestForm()
    if form.validate_on_submit():

	name = form.name.data
	message = form.message.data
	
	guest = Guest(name, message)
	db.session.add(guest)
	db.session.commit()

	return redirect("/")
    
    return render_template("add_guest.html", form=form)
