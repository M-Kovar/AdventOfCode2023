# Advent of Code 2023
# https://adventofcode.com/2023/day/2

import os
# Change working directory to where this script is saved
os.chdir(os.path.dirname(__file__))

# --- End of header and initialization -----------------

def get_input(input_path):
    with open(input_path, "r") as file:
        return [line.strip() for line in file]

class Games():

    def __init__(self, games_def_list):
        self.games = [Game(game_def) for game_def in games_def_list]

    def get_possible(self, test_draw):
        return [game.id for game in self.games if game.is_possible(test_draw)]
    
    def get_powers(self):
        return [game.get_power() for game in self.games]
    

class Game():

    def __init__(self, game_def):
        game_def = game_def.replace(";", ",")
        game, draws = game_def.split(": ")
        _, game_id_str = game.split(" ")
        self.id = int(game_id_str)
        self.cubes_count = self.count_cubes(draws)

    def count_cubes(self, draws):
        cubes_count = dict()
        for draw in draws.split(", "):
            amount, color = draw.split(" ")
            if color not in cubes_count:
                cubes_count[color] = 0
            cubes_count[color] = max(cubes_count[color], int(amount))
        return cubes_count
    
    def is_possible(self, test_draw):
        possible = True
        for color in test_draw:
            if test_draw[color] < self.cubes_count[color]:
                possible = False
        return possible
    
    def get_power(self):
        power = 1
        for num in self.cubes_count.values():
            power *= num
        return power


if __name__ == "__main__":

    input_path = "input.txt"
    games_def_input = get_input(input_path)

    games = Games(games_def_input)

    test_draw = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    # Part 1:
    part1 = sum(games.get_possible(test_draw))
    print(f"Part 1: {part1}")

    # Part 2:
    part2 = sum(games.get_powers())
    print(f"Part 2: {part2}")