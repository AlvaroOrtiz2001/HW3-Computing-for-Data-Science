import pytest
from hw4 import Deck  

def test_shuffle_deck():
    deck = Deck()
    original_order = deck.cards.copy()
    deck.shuffle()
    assert original_order != deck.cards

def test_draw_card():
    deck = Deck()
    card = deck.draw()
    assert card is not None

def test_draw_card_empty():
    deck = Deck()
    # Draw all cards to make the deck empty
    for i in range(52):
        deck.draw()
    assert deck.draw() is None
