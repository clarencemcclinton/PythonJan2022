from flask_app import app
from flask import render_template, redirect, session, request

from flask_app.models.user import User

# =============================================
# Read All
# =============================================
@app.route('/')
def index():
    users = User.all_users()
    print(users)
    for user in users:
        print(user.first_name)
    return render_template('index.html', users = users)

# =============================================
# Read One route
# =============================================
@app.route("/<int:user_id>")
def one_user(user_id):
    # call on get_one_user query
    data = {
        "user_id" : user_id
    }
    user = User.one_user(data)
    print(user)
    return render_template("show_user.html", user = user)

# =============================================
# Create Routes
# =============================================
@app.route("/new_user")
def new_user():
    return render_template("new_user.html")

@app.route("/add_user", methods=["POST"])
def add_user():
    # 1 - collect the info from the form
    # first_name = request.form['first_name']
    # last_name = request.form['last_name']
    # handle = request.form['handle']
    # birthday = request.form['birthday']
    # age = request.form['age']
    # 2 - repackage info into data to send to query
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "handle" : request.form['handle'],
        "birthday" : request.form['birthday'],
        "age" : request.form['age']
    }
    # 3 - call on query
    new_user_id = User.create_user(data)

    # 4 - if successful, redirect to a render route
    return redirect("/")