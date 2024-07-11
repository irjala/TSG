import random

from cards.deck import Deck
from game_settings.settings import win_condition
from players.player import Player


def gameplay_loop(players):
    # Choose a random player to be first
    first_player_index = random.randint(0, len(players) - 1)

    # Reorganize the order of the players
    players = players[first_player_index:] + players[:first_player_index]

    # Start the game on turn 1
    turn = 1

    while True:
        # Each player takes their turn
        for player in players:
            print("Turn:", turn)
            print(player.name)
            player.res6 += 5

            if player.res6 >= 20:
                draw_card(player)
                return

            # Check if the game is over
            if win_condition():
              print(player.name + " Wins!")
              break
            else:
              print(player.name + " Resources: " + player.res6)

        # Increment the turn
        turn += 1