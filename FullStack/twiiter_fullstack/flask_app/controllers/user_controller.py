from flask_app import app
from flask import render_template, redirect, session, request

from flask_app.models.user import User

# =============================================
# Read All
# =============================================
@app.route('/')
def index():
    #1 - Call on your query in your model file
    users = User.all_users()
    #1a - see the info you've pulled via the query and parsed into objects
    print(users)
    # for user in users:
    #     print(user.first_name)

        #2 - render your template, and pass the information from your backend to the HTML
    return render_template('index.html', users = users)

# =============================================
# Read One route
# =============================================
@app.route("/<int:user_id>")
def one_user(user_id):
    #1 - collect the info you need to run your query
    #  - in this case you just need the id of the user you are trying to find!
    #  - the key is going to be what we call on in the query itself
    data = {
        "user_id" : user_id
    }

    #2 - call on the query and pass in the data you need
    user = User.one_user(data)

    #2a - see the info you've pulled via the query and parsed into objects
    print(user)

    #3 - render your template, and pass the information from your backend to the HTML
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