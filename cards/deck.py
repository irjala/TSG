from card import *


''' Deck functions '''

def generate_deck():
  first_card = Card(name="Mega card", special=card_func_firstcard())
  second_card = Card(name="Second card", special=card_func_secondcard())

  deck = [first_card, second_card]
  return deck
