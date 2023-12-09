# Advent of Code 2023
# https://adventofcode.com/2023/day/9

import os
# Change working directory to where this script is saved
os.chdir(os.path.dirname(__file__))

# --- End of header and initialization -----------------

def get_input(input_path):
    with open(input_path, "r") as file:
        lines = []
        for line in file:
            values = line.strip().split()
            lines.append([int(v) for v in values])
    return lines

def diff(values):
    return [val2-val1 for val1,val2 in zip(values,values[1:])]

def predict(values, predict_past=False):
    edge_values = []
    while not all(v==0 for v in values):
        edge = values[0] if predict_past else values[-1]
        edge_values.append(edge)
        values = diff(values)
    prediction = 0
    for value in edge_values[::-1]:
        if predict_past:
            prediction = value - prediction
        else:
            prediction = value + prediction
    return prediction


if __name__ == "__main__":

    input_path = "input.txt"
    input_lines = get_input(input_path)

    # Part 1:
    predictions = [predict(line) for line in input_lines]
    part1 = sum(predictions)
    print(f"Part 1: {part1}")

    # Part 2:
    predictions2 = [predict(line,predict_past=True) for line in input_lines]
    part2 = sum(predictions2)
    print(f"Part 2: {part2}")