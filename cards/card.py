import random


''' Card class '''

class Card:
  def __init__(self, name, cost=0, val1=0, val2=0, val3=0, special=None):
    if name == None:
      raise ValueError("Card name cannot be None")
    self.name = name
    self.cost = cost
    self.val1 = val1
    self.val2 = val2
    self.val3 = val3
    self.special = special


''' Card specialty functions '''

def card_func_firstcard():
  print("You did the function!")

def card_func_secondcard(players):
  robbed = players[random.int]
  robbed.res6 -= 3
  print(robbed.name + " got robbed for 3!")


''' Game call functions '''

def draw_card(player):
  drawn_card = random.choice(game_deck.cards)
  for cards in player.cards:
    if cards.special != None:
      cards.special()
  player.cards.remove(card)
  return card

def remove_card(player, card):
  player.cards.remove(card)
  if player.res6 >= 30:
    return True
  else:
    return False
