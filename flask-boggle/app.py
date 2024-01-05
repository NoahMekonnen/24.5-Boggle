from boggle import Boggle
from flask import Flask, request, render_template, session, redirect, jsonify
from flask_debugtoolbar import DebugToolbarExtension
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
app.config['TESTING'] = True
# app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

debug = DebugToolbarExtension(app)

app.debug = True

boggle_game = Boggle()

session['num_of_games'] = 0

"""Starts a Boggle Game"""
@app.route('/')
def welcome():
    new_board = boggle_game.make_board()
    session['new_board'] = new_board
    session['num_of_games'] +=1
    return render_template('base.html', new_board = new_board)

"""Starts Game and accepts post request of score"""
@app.route('/', methods = ['POST'])
def post_request():
    print(request.json, "home")
    new_board = boggle_game.make_board()
    session['new_board'] = new_board
    session['num_of_games'] +=1
    return render_template('base.html', new_board = new_board)

"""Checks if word is valid"""
@app.route('/check-word', methods = ['POST'])
def check_guess():
    guess = request.json['params']['guess'] 
    valid_word = boggle_game.check_valid_word(session['new_board'], guess)
    return jsonify({'result': valid_word})