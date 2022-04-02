import unittest

from src.card import Card
from src.card_game import *

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card_game = CardGame()
        self.card1 = Card('hearts', 4)
        self.card2 = Card('spades', 1)
        self.card3 = Card('clubs', 10)
        self.card4 = Card('diamonds', 12)
        self.cards = [self.card1, self.card2, self.card3, self.card4]
    

    def test_check_for_ace (self):
        self.assertEqual(True, self.card_game.check_for_ace(self.card2))
    
    def test_highest_card (self):
        self.assertEqual(self.card1, self.card_game.highest_card(self.card1, self.card2))

    def test_cards_total (self):
        self.assertEqual("You have a total of 27", self.card_game.cards_total(self.cards))

    
