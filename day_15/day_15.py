# Advent of Code 2023
# https://adventofcode.com/2023/day/15

import os
# Change working directory to where this script is saved
os.chdir(os.path.dirname(__file__))

# --- End of header and initialization -----------------

def get_input(input_path):
    with open(input_path, "r") as file:
        return file.read().split(",")

def get_hash_value(instruction):
    value = 0
    for char in instruction:
        value += ord(char)
        value *= 17
        value %= 256
    return value

if __name__ == "__main__":

    input_path = "input.txt"
    instructions = get_input(input_path)
    hash_values = [get_hash_value(instruction) for instruction in instructions]

    # Part 1:
    part1 = sum(hash_values)
    print(f"Part 1: {part1}")

    # Part 2:
    # part2 = sum(hash_values)
    # print(f"Part 2: {part2}")