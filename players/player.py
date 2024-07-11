import random

class Player:
  def __init__(self, name="player" + str(random.randint(100000, 999999)),
               res1=0, res2=0, res3=0, res4=0, res5=0, res6=0,
               cards=[], action1=False, action2=False):
    self.name = name
    self.res1 = res1
    self.res2 = res2
    self.res3 = res3
    self.res4 = res4
    self.res5 = res5
    self.res6 = res6
    self.cards = cards
    self.action1 = action1
    self.action2 = action2

  def add_card(self, card):
    self.cards.append(card)

  def remove_card(self, card):
    self.cards.remove(card)