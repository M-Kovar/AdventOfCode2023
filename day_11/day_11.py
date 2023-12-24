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

def expand(space_map, expansion_factor, galaxy_symbol="#"):
    # Capture distances in space: 1 if galaxy is present, expand space if not
    distances_rows = [expansion_factor if galaxy_symbol not in row else 1 for row in space_map]
    # zip(*matrix) generates a transposed version of a matrix
    distances_cols = [expansion_factor if galaxy_symbol not in col else 1 for col in zip(*space_map)]
    return distances_rows, distances_cols

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

def get_galaxy_distances(galaxies, expanded_distances):
    galaxy_pairs = get_pair_combinations(galaxies.keys())
    distances = [calc_shortest_dist(galaxies[gal1_id], galaxies[gal2_id], expanded_distances) for gal1_id, gal2_id in galaxy_pairs]
    return distances

def calc_shortest_dist(coords1, coords2, distances):
    # Manhattan distance
    x1, y1 = coords1
    x2, y2 = coords2
    if x1 > x2:
        x2,x1 = x1,x2
    if y1 > y2:
        y2,y1 = y1,y2
    dist_rows, dist_cols = distances
    return sum(dist_rows[x1:x2]) + sum(dist_cols[y1:y2])


if __name__ == "__main__":

    input_path = "input.txt"
    space_map = get_input(input_path)
    galaxies = find_galaxies(space_map)

    # Part 1:
    space_expanded = expand(space_map, expansion_factor=2)
    distances = get_galaxy_distances(galaxies, space_expanded)

    part1 = sum(distances)
    print(f"Part 1: {part1}")

    # Part 2:
    space_expanded2 = expand(space_map, expansion_factor=1000000)
    distances2 = get_galaxy_distances(galaxies, space_expanded2)

    part2 = sum(distances2)
    print(f"Part 2: {part2}")