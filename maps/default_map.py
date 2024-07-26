import csv
import os
from game_settings import settings

class IslandMap:
    def __init__(self, size=20):
        
        self.size = size
        self.map = self.generate_map()

    def generate_map(self):
    
        size = self.size
        full_map = [[[None, None, None, None] for _ in range(self.size)] for _ in range(self.size)]
        playable_terrain = self.read_csv_to_matrix(os.path.join('.', 'maps', 'island_map.csv'))
    
    def read_csv_to_matrix(self, csv_file):
        matrix = []
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                matrix.append([int(value) for value in row])
        return matrix

    def integrate_matrix(self, matrix):
        for i in range(self.size):
            for j in range(self.size):
                self.map[i][j][0] = matrix[i][j]

    def display_map(self):
        
        for row in self.map:
            print(' '.join(map(str, row)))


    def display_board(self):
        """
        Displays the hexagonal board.
        """
        for row in self.board:
            print(row)
