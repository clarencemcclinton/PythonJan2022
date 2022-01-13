from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/hello/<name>')
def hello(name):
    return f'Hello {name}!'


@app.route('/<int:number>')
def number(number):
    newNum = number * 5
    return f"the new number is {newNum}"

















if __name__=="__main__":
    app.run(debug=True)
