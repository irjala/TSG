import random

from cards.deck import *
from cards.card import *
from game_settings.settings import win_condition
from players.player import *
from game_instance import *


def gameplay_loop(players):
    # Choose a random player to be first
    first_player_index = random.randint(0, len(players) - 1)

    # Reorganize the order of the players
    players = players[first_player_index:] + players[:first_player_index]

    main_deck = create_deck_from_csv('cards/main_cards.csv')
    for i in main_deck:
      print(f'Name: {i.name}, Cost: {i.cost}, Val1: {i.val1}, Val2: {i.val2}, Val3: {i.val3}, Special: {i.special}')
    # Start the game on turn 1
    turn = 1

    while True:
        # Each player takes their turn
        for player in players:
            print("Turn:", turn)
            print(player.name)

            if turn == 1:
              print("It is the first turn!")
              first_turn(player)

            player.res6 += 5

            if player.res6 >= 20:
                draw_card(player)
                return

            # Check if the game is over
            if win_condition(player):
              print(player.name + " Wins!")
              break
            else:
              print(player.name + " Resources: " + player.res6)

        # Increment the turn
        turn += 1

player_list = [Player(), Player()]
gameplay_loop(player_list)