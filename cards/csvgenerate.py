import csv
import random
import string
import os

def generate_random_card_name():
    return ''.join(random.choices(string.ascii_letters, k=8))

def generate_random_cost():
    return random.randint(1, 100)

def generate_random_resource():
    return random.choice(['wood', 'stone', 'gold', 'silver', 'iron'])

def generate_random_space():
    return random.choice(['land', 'sea', 'air', 'space'])

def generate_random_special():
    return random.choice(['none', 'fire', 'water', 'earth', 'wind'])

def generate_csv(file_name):
    # Create subfolder if it doesn't exist
    subfolder = "cards"
    os.makedirs(subfolder, exist_ok=True)

    fieldnames = ["card_name", "cost", "resource", "space", "special"]
    rows = [
        {
            "card_name": generate_random_card_name(),
            "cost": generate_random_cost(),
            "resource": generate_random_resource(),
            "space": generate_random_space(),
            "special": generate_random_special()
        } for _ in range(5)
    ]

    # Construct the full path for the file
    file_path = os.path.join(subfolder, file_name)
    
    with open(file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

# Generate and save the CSV file in the 'cards' subfolder
generate_csv("cards.csv")