import random
import string

from cards import deck
from players.player import Player

def generate_game_id(length=20):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

class Game:
  def __init__(self, turn=1, player_order=None, res3=0, res4=0, res5=0, res6=0, guild=None,
               cards=None, action1=False, action2=False):
    self.id = generate_game_id()
    self.main_deck = deck.create_deck_from_csv('cards')
    self.gobbs_deck = deck.create_deck_from_csv('gobbs_cards')
    self.lobster_deck = deck.create_deck_from_csv('lobster_cards')
    self.turn = turn
    self.player_order = player_order if player_order is not None else []
    self.cards = cards if cards is not None else []

  def turn_check(self, card):
    # Placeholder print
    print("Here will be the logic for checking and changing turns")

  def add_player(self, player_name):
        new_player = Player(player_name)
        self.player = new_player
        self.player_order.append(new_player.name)

  def add_card(self, card):
    self.cards.append(card)

  def remove_card(self, card):
    self.cards.remove(card)

  def shuffle_deck(self, deck):
    randomized_deck = deck[:]
    random.shuffle(randomized_deck)
    return randomized_deck

  def shuffle_player_order(self):
    random.shuffle(self.player_order)
  