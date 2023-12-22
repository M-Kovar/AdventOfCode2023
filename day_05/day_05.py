# Advent of Code 2023
# https://adventofcode.com/2023/day/5

import os
# Change working directory to where this script is saved
os.chdir(os.path.dirname(__file__))

# --- End of header and initialization -----------------

def get_input(input_path):
    with open(input_path, "r") as file:
        return [line.strip() for line in file]

def parse_almanac(lines):
    almanac = dict()
    _, seeds = lines.pop(0).split(":")
    almanac["seeds"] = [int(num) for num in seeds.split()]
    for line in lines:
        if not line:
            continue
        first_char = line[0]
        if first_char.isalpha():
            item_name, _ = line.split(":")
            almanac[item_name] = []
        elif first_char.isnumeric():
            almanac[item_name].append( [int(num) for num in line.split()] )
    return almanac

def map_seed(seed, almanac):
    for values_list in almanac.values():
        for val_map in values_list:
            destination, source, rng = val_map
            source_rng = range(source, source+rng)
            shift = destination - source
            if seed in source_rng:
                # print(key)
                seed += shift
                break
    location = seed
    return location

def parse_seeds(seeds):
    # (naive approach infeasible - to be optimized)
    seeds_parsed = []
    seeds = iter(seeds)
    for seed_start in seeds:
        seed_end = next(seeds)
        if seed_start > seed_end:
            seed_end, seed_start = seed_start, seed_end
        # print(seed_start)
        # print(seed_end)
        seed_rng = range(seed_start, seed_end+1)
        seeds_parsed.extend(seed_rng)
    return seeds_parsed


if __name__ == "__main__":

    input_path = "input.txt"
    input_lines = get_input(input_path)

    almanac = parse_almanac(input_lines)
    # print(almanac)
    seeds = almanac.pop("seeds")
    locations = [map_seed(seed, almanac) for seed in seeds]

    # Part 1:
    part1 = min(locations)
    print(f"Part 1: {part1}")

    # Part 2:
    # (naive approach infeasible - to be optimized)
    # seeds2 = parse_seeds(seeds)
    # locations2 = [map_seed(seed, almanac) for seed in seeds2]
    # part2 = min(locations2)
    # print(f"Part 2: {part2}")