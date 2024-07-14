import random

from cards.deck import *
from cards.card import *
from game_settings.settings import win_condition
from players.player import *
import game_instance


def start_game(players):
    
    player_names = ['Simon', 'John', 'Franz']
    
    # Init the game
    current_game = game_instance.Game()

    for i in players:
      current_game.add_player(i)

    current_game.shuffle_player_order()

    check_player = current_game.player_order
    print(check_player)
    
    current_game.shuffle_deck('main_deck')
    current_game.shuffle_deck('gobbs_deck')
    current_game.shuffle_deck('lobster_deck')
    
    for i in current_game.main_deck:
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
              #first_turn(player)

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
start_game(player_list)