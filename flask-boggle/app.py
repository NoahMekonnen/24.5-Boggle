from boggle import Boggle
from flask import Flask, request, render_template, session, redirect, jsonify
from flask_debugtoolbar import DebugToolbarExtension
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

debug = DebugToolbarExtension(app)

app.debug = True

boggle_game = Boggle()


@app.route('/')
def welcome():
    """Starts a Boggle Game"""
    new_board = boggle_game.make_board()
    session['new_board'] = new_board
    num_of_plays = session.get("num_of_plays",0)
    return render_template('base.html', new_board = new_board, num_of_plays = num_of_plays)


@app.route('/check-word')
def check_guess():
    """Checks if word is valid"""
    guess = request.args['guess']
    valid_word = boggle_game.check_valid_word(session['new_board'], guess)
    return jsonify({'result': valid_word})


@app.route('/update-num-of-games', methods = ['POST'])
def update_score():
    """Keeps track of number of games played"""
    session['num_of_plays'] +=1
    return redirect('/')