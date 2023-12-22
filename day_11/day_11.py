# Advent of Code 2023
# https://adventofcode.com/2023/day/11

import os
# Change working directory to where this script is saved
os.chdir(os.path.dirname(__file__))

# --- End of header and initialization -----------------

import itertools

def get_input(input_path):
    with open(input_path, "r") as file:
        return [line.strip() for line in file]

def expand(space_map, galaxy_symbol="#"):
    empty_rows = [idx for idx,row in enumerate(space_map) if galaxy_symbol not in row]
    # zip(*matrix) generates a transposed version of a matrix
    empty_cols = [idx for idx,col in enumerate(zip(*space_map)) if galaxy_symbol not in col]
    for shift,idx in enumerate(empty_rows):
        space_map.insert(idx+shift, space_map[idx+shift])
    # Transpose to add the column-wise expansions
    space_map_transposed = ["".join(x) for x in zip(*space_map)]
    for shift,idx in enumerate(empty_cols):
        space_map_transposed.insert(idx+shift, space_map_transposed[idx+shift])
    # Transpose back
    return ["".join(x) for x in zip(*space_map_transposed)]

def find_galaxies(space_map, galaxy_symbol="#"):
    galaxy_id = 1
    galaxies = dict()
    for idx_row, row in enumerate(space_map):
        for idx_col, symbol in enumerate(row):
            if symbol == galaxy_symbol:
                galaxies[galaxy_id] = (idx_row, idx_col)
                galaxy_id += 1
    return galaxies

def get_pair_combinations(numbers):
    return itertools.combinations(numbers, 2)

def get_galaxy_distances(galaxies):
    galaxy_pairs = get_pair_combinations(galaxies.keys())
    distances = [calc_shortest_dist(galaxies[gal1_id], galaxies[gal2_id]) for gal1_id, gal2_id in galaxy_pairs]
    return distances

def calc_shortest_dist(coords1, coords2):
    # Manhattan distance
    x1, y1 = coords1
    x2, y2 = coords2
    return abs(x2-x1) + abs(y2-y1)


if __name__ == "__main__":

    input_path = "input.txt"
    space_map = get_input(input_path)
    space_map = expand(space_map)

    galaxies = find_galaxies(space_map)
    distances = get_galaxy_distances(galaxies)

    # Part 1:
    part1 = sum(distances)
    print(f"Part 1: {part1}")

    # Part 2:
    # part2 = sum(distances)
    # print(f"Part 2: {part2}")