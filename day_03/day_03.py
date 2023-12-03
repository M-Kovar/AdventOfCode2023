# Advent of Code 2023
# https://adventofcode.com/2023/day/3

import os
# Change working directory to where this script is saved
os.chdir(os.path.dirname(__file__))

# --- End of header and initialization -----------------

import re

def get_input(input_path):
    with open(input_path, "r") as file:
        return [line.strip() for line in file]
    
def get_matches(line, regex):
    return re.finditer(regex, line)

def get_number_matches(line):
    # Match one or more digits
    return get_matches(line, r'\d+')

def get_symbol_matches(line):
    # Match everything except dots and digits
    return get_matches(line, r'[^\.\d]')

def get_star_matches(line):
    return get_matches(line, r'\*')

def get_lines_block(lines, i_middle):
    num_lines = len(lines)
    prev_line = lines[i_middle-1] if i_middle > 0 else ''
    main_line = lines[i_middle]
    next_line = lines[i_middle+1] if i_middle < num_lines-1 else ''
    return [prev_line, main_line, next_line]

def is_adjacent(number_span, symbol_span):
    symbol_pos = symbol_span[0]
    # span[1] index is exclusive (beyond the match)
    return number_span[0]-1 <= symbol_pos <= number_span[1]

def get_part_numbers(txt_lines):
    part_numbers = []
    num_lines = len(txt_lines)
    for i in range(0,num_lines):
        # lines_block = [prev_line, main_line, next_line]
        lines_block = get_lines_block(txt_lines, i)
        number_matches = get_number_matches(lines_block[1])
        for number_match in number_matches:
            number_value = int(number_match.group())
            for line in lines_block:
                for symbol_match in get_symbol_matches(line):
                    if is_adjacent(number_match.span(), symbol_match.span()):
                        part_numbers.append(number_value)
                        break
    return part_numbers

def get_gear_ratios(txt_lines):
    gear_ratios = []
    num_lines = len(txt_lines)
    for i in range(0,num_lines):
        lines_block = get_lines_block(txt_lines, i)
        star_matches = get_star_matches(lines_block[1])
        for star_match in star_matches:
            values_per_star = []
            for line in lines_block:
                for number_match in get_number_matches(line):
                    if is_adjacent(number_match.span(), star_match.span()):
                        number_value = int(number_match.group())
                        values_per_star.append(number_value)
            if len(values_per_star) == 2:
                gear_ratios.append(values_per_star[0] * values_per_star[1])
    return gear_ratios


if __name__ == "__main__":

    input_path = "input.txt"
    txt_lines = get_input(input_path)

    # Part 1:
    part_numbers = get_part_numbers(txt_lines)
    part1 = sum(part_numbers)
    print(f"Part 1: {part1}")

    # Part 2:
    gear_ratios = get_gear_ratios(txt_lines)
    part2 = sum(gear_ratios)
    print(f"Part 2: {part2}")