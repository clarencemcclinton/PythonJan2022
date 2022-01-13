from flask import Flask, render_template
app = Flask(__name__)


@app.route('/<name>')
def index(name):
    print(f"The name is: {name}")
    return render_template('index.html', name=name, num=8)

@app.route("/advanced/<color>")
def advanced(color):

    student_info = [
        {'name' : 'Michael', 'age' : 35},
        {'name' : 'John', 'age' : 30 },
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    ]

    return render_template("adv.html", students = student_info, color=color)


@app.route("/httpresponse")
def http():
    return "This is a Http Response"





if __name__=="__main__":
    app.run(debug=True)