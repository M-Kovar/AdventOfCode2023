# Advent of Code 2023
# https://adventofcode.com/2023/day/6

import os
# Change working directory to where this script is saved
os.chdir(os.path.dirname(__file__))

# --- End of header and initialization -----------------

def get_input(input_path):
    with open(input_path, "r") as file:
        return [line.strip() for line in file]

def parse_data(lines, fix_kerning=False):
    data = dict()
    for line in lines:
        name, values_raw = line.split(":")
        values = [int(num) for num in values_raw.split()]
        if fix_kerning:
            values = [ int("".join(values_raw.split())) ]
        data[name] = values
    return data

def count_win_options(time_ref, distance_ref):
    charge_options = range(0,time_ref+1)
    win_counter = 0
    for chrg in charge_options:
        speed = chrg
        time_move = time_ref - chrg
        distance = speed * time_move
        if distance > distance_ref:
            win_counter += 1
    # ... can be optimized, but ain't nobody got time fo dat
    return win_counter

def count_win_score(data_dict):
    win_score = 1
    for t,d in zip(data_dict["Time"], data_dict["Distance"]):
        win_score *= count_win_options(t, d)
    return win_score


if __name__ == "__main__":

    input_path = "input.txt"
    input_lines = get_input(input_path)

    # Part 1:
    data1 = parse_data(input_lines)
    part1 = count_win_score(data1)
    print(f"Part 1: {part1}")

    # Part 2:
    data2 = parse_data(input_lines, fix_kerning=True)
    part2 = count_win_score(data2)
    print(f"Part 2: {part2}")