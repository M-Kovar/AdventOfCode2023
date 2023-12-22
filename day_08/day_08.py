# Advent of Code 2023
# https://adventofcode.com/2023/day/8

import os
# Change working directory to where this script is saved
os.chdir(os.path.dirname(__file__))

# --- End of header and initialization -----------------

import re

def get_input(input_path):
    with open(input_path, "r") as file:
        return [line.strip() for line in file]
    
def parse_input(lines):
    directions = list(lines[0])
    nodes = dict()
    for line in lines[2:]:
        triplets = re.findall(r"\w{3}", line)
        nodes[triplets[0]] = tuple(triplets[1:])
    return directions, nodes

def count_steps(directions, nodes, start="AAA", destination="ZZZ"):
    left_right_idx = {"L": 0, "R": 1}
    node = start
    dir_nodes = nodes[node]
    steps = 0
    while node != destination:
        for lr in directions:
            node = dir_nodes[left_right_idx[lr]]
            dir_nodes = nodes[node]
            steps += 1
            if node == destination:
                break
    return steps


if __name__ == "__main__":

    input_path = "input.txt"
    input_lines = get_input(input_path)
    directions, nodes = parse_input(input_lines)

    # Part 1:
    part1 = count_steps(directions, nodes)
    print(f"Part 1: {part1}")

    # Part 2:
    # part2 = count_steps_part2(directions, nodes)
    # print(f"Part 2: {part2}")