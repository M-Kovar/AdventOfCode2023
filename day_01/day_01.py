# Advent of Code 2023
# https://adventofcode.com/2023/day/1

import os
# Change working directory to where this script is saved
os.chdir(os.path.dirname(__file__))

# --- End of header and initialization -----------------

import re

def get_input(input_path):
    with open(input_path, "r") as file:
        return [line.strip() for line in file]

def raw_to_numeric(digits_raw):
    digits_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    # .get(digit,digit) inserts the original numeric digit (as it is not in the digits_dict)
    return [digits_dict.get(digit,digit) for digit in digits_raw]

def get_first_last_value(line, find_word_digits=False):
    if find_word_digits:
        # ?= is a lookahead assertion, practically ensuring that even overlapping
        # values are captured. E.g. "oneight" finds "one" and "eight"
        regex = r'(?=([1-9]|one|two|three|four|five|six|seven|eight|nine))'
    else:
        regex = r'[1-9]'
    digits_raw = re.findall(regex, line)
    digits_numeric = raw_to_numeric(digits_raw)
    return int(digits_numeric[0] + digits_numeric[-1])
    

if __name__ == "__main__":

    input_path = "input.txt"
    input_lines = get_input(input_path)

    # Part 1:
    values_first_last_part1 = [get_first_last_value(line) for line in input_lines]
    part1 = sum(values_first_last_part1)
    print(f"Part 1: {part1}")

    # Part 2:
    values_first_last_part2 = [get_first_last_value(line,find_word_digits=True) for line in input_lines]
    part2 = sum(values_first_last_part2)
    print(f"Part 2: {part2}")