from boggle import Boggle
from flask import Flask, request, render_template, session, redirect
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

debug = DebugToolbarExtension(app)

app.debug = True

boggle_game = Boggle()
# session['score'] = 0

@app.route('/')
def welcome():
    new_board = boggle_game.make_board()
    session['new_board'] = new_board
    return render_template('base.html', new_board = new_board)

@app.route('/guesses')
def check_guess():
    guess_in_words = guess in boggle_game.words
    guess = request.form.get('guess')
    # valid_word = boggle_game.check_valid_word(new_board, guess)
    return redirect('/')