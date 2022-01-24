from flask_app import app
from flask import render_template, request, session, redirect

from flask_app.models.owner import Owner

@app.route("/")
def index():

    owners_with_pets = Owner.owners_with_pets()
    return render_template("index.html", owners = owners_with_pets)

@app.route("/<int:owner_id>")
def show_one_owner(owner_id):
    data = {
        "owner_id" : owner_id
    }

    one_owner = Owner.get_one_owner(data)
    return render_template("show_one.html", owner = one_owner)
