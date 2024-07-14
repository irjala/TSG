import random
import os
import csv
from .card import *

''' Hardcoded placeholders '''

main_deck = [0,1,2,3,4,5,6,7,8,9]
gobbs_deck = [0,1,2,3]
lobsters_deck = [0,1,2,3]


''' Deck functions '''

def create_deck_from_csv(deck_name):
    
    ### TEST ###
    test_card = Card(name="test")
    main_deck = [test_card]
    csv_file_path = os.path.join('cards', f'{deck_name}.csv')
    
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Extract values from the row, converting to appropriate types
            name = row['card_name']
            cost = int(row['cost']) if row['cost'] else 0
            val1 = int(row['resource']) if row['resource'] else 0
            val2 = int(row['space']) if row['space'] else 0
            val3 = 0  # Assuming val3 is not provided in the CSV, set it to 0
            special = row['special'] if row['special'] else None
            
            # Create a Card instance and add it to the main_deck
            card = Card(name, cost, val1, val2, val3, special)
            main_deck.append(card)
    
    return main_deck

def randomize_order(deck_list):
    randomized_list = deck_list[:]
    random.shuffle(randomized_list)
    return randomized_list


def draw_card(deck_name):
    cards_list = deck_name
    if cards_list:
        next_card = cards_list[0]
        card = fetch_card(deck_name, next_card)
        cards_list.pop(0)
        return
