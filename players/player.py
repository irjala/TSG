import random

class Player:
  def __init__(self, name="player" + str(random.randint(100000, 999999)),
               res1=0, res2=0, res3=0, res4=0, res5=0, res6=0, guild=None,
               cards=[], action1=False, action2=False):
    self.name = name
    self.res1 = res1
    self.res2 = res2
    self.res3 = res3
    self.res4 = res4
    self.res5 = res5
    self.res6 = res6
    self.guild = guild
    self.cards = cards
    self.action1 = action1
    self.action2 = action2

  def add_card(self, card):
    self.cards.append(card)

  def remove_card(self, card):
    self.cards.remove(card)


def first_turn(player):
    while True:
        try:
            guild_int = int(input("Choose guild\n1 = Gobbs\n2 = Lobsters\n3 = Random\n"))
            if 1 <= guild_int <= 3:
                player.guild = guild_int
                break
            else:
                print("Please pick a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 3.")

