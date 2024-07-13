import random
import string

from players import player
from cards import deck

def generate_game_id(length=20):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

class Game:
  def __init__(self, turn=1, player_count=2, res3=0, res4=0, res5=0, res6=0, guild=None,
               cards=[], action1=False, action2=False):
    self.id = generate_game_id()
    self.turn = turn
    self.player_count = player_count
    
    self.main_deck_order = [0,1,2,3,4,5]

  def add_card(self, card):
    self.cards.append(card)

  def remove_card(self, card):
    self.cards.remove(card)
