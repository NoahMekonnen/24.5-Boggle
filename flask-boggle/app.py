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

"""Starts a Boggle Game"""
@app.route('/')
def welcome():
    new_board = boggle_game.make_board()
    # if not session['num_of_plays']:
    #     session["num_of_plays"] = 0
    session['new_board'] = new_board
    num_of_plays = session.get("num_of_plays",0)
    return render_template('base.html', new_board = new_board, num_of_plays = num_of_plays)

"""Checks if word is valid"""
@app.route('/check-word', methods = ['POST'])
def check_guess():
    guess = request.json['params']['guess'] 
    valid_word = boggle_game.check_valid_word(session['new_board'], guess)
    return jsonify({'result': valid_word})

"""Keeps track of number of games played"""
@app.route('/update-num-of-games', methods = ['POST'])
def update_score():
    session['num_of_plays'] +=1
    print(session['num_of_plays'])
    return redirect('/')