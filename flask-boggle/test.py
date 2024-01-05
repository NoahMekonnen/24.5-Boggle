from unittest import TestCase
from app import app
from flask import session,jsonify,request
from boggle import Boggle
import json


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!
    # def setUp(self):
    #   """Stuff to do before every test."""
    #   with app.test_client() as client:
    #     with client.session_transaction() as change_session:
    #         change_session["num_of_plays"] = 0
    #         boggle_game = Boggle()
    #         new_board = boggle_game.make_board()
    #         change_session["new_board"] = new_board
    

    # def tearDown(self):
    #   """Stuff to do after each test."""
    def test_welcome(self):
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("Score :", html)

    def test_check_guess(self):
        boggle_game = Boggle()
        new_board = boggle_game.make_board()
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session['new_board']= new_board
            resp = client.get('/check-word?guess=SAINTS')
            html = resp.get_data(as_text=True)
            self.assertEqual('not-a-word', resp.json['result'])

    def test_update_score(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session["num_of_plays"] = 0
            resp = client.post('/update-num-of-games',data ={'score': 3})
            html = resp.get_data(as_text=True)
            self.assertEqual(session["num_of_plays"], 1)