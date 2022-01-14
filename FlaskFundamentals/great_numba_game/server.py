from flask import Flask, render_template, redirect, session, request
import random
app = Flask(__name__)
app.secret_key = "jghfkd;sunhgfdop"


@app.route('/')
def index():
    if 'computer_guess' not in session:
        session['computer_guess'] = random.randint(1, 100)
        session['guess_count'] = 0
    print(session['computer_guess'])
    count = session['guess_count']
    guess = None
    location = None

    if 'guess' in session:
        guess = session['guess']
        location = session['location']
    
    return render_template('index.html', guess=guess, location=location, count=count)

@app.route('/process_guess', methods=['POST'])
def process():
    # print(request.form)
    guess = int(request.form['guess'])
    session['guess'] = guess

    comp = int(session['computer_guess'])
    
    # increment our count of guesses!
    session['guess_count'] = int(session['guess_count']) + 1

    if guess > comp:
        print('Your guess is too high!')
        session['location'] = 'high'

    if guess < comp:
        print('You guess is too low!')
        session['location'] = 'low'

    if guess == comp:
        print('Right on the money!')
        session['location'] = 'correct'
    return redirect('/')

@app.route("/restart")
def restart():
    session.clear()
    return redirect('/')







if __name__=="__main__":
    app.run(debug=True)