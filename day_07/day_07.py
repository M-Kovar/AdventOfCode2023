# Advent of Code 2023
# https://adventofcode.com/2023/day/7

import os
# Change working directory to where this script is saved
os.chdir(os.path.dirname(__file__))

# --- End of header and initialization -----------------

from collections import Counter

def get_input(input_path):
    with open(input_path, "r") as file:
        return [line.strip() for line in file]
    
class Hand():

    symbol_order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

    def __init__(self, hand_def):
        cards, bid = hand_def.split()
        self.cards = list(cards)
        self.bid = int(bid)
        self.type = self.get_type()

    def get_type(self):
        counter = Counter(self.cards)
        counts_common = counter.most_common()
        _, count_most = counts_common.pop(0)
        if counts_common:
            _, count_2nd = counts_common.pop(0)
        # Switch (match-case) implemented in Python 3.10+
        match count_most:
            case 5:
                type = "Five of a kind"
            case 4:
                type = "Four of a kind"
            case 3:
                type = "Full house" if count_2nd == 2 else "Three of a kind"
            case 2:
                type = "Two pairs" if count_2nd == 2 else "One pair"
            case 1:
                type = "High card"
        return type

    def sort_cards(self):
        return sorted(self.cards, key=lambda x: self.symbol_order.index(x))

class Deck():

    types_order = [
            "Five of a kind", 
            "Four of a kind", 
            "Full house", 
            "Three of a kind", 
            "Two pairs", 
            "One pair", 
            "High card"
            ]

    def __init__(self, hands):
        self.hands = [Hand(hand_def) for hand_def in hands]

    def get_scores(self):
        ranks = range(len(self.hands), 0, -1)
        return [hand.bid*rank for hand,rank in zip(self.get_sorted_deck(), ranks)]

    def get_sorted_deck(self):
        sorting_keys = lambda x: (self.types_order.index(x.type),
                                  x.symbol_order.index(x.cards[0]),
                                  x.symbol_order.index(x.cards[1]),
                                  x.symbol_order.index(x.cards[2]),
                                  x.symbol_order.index(x.cards[3]),
                                  x.symbol_order.index(x.cards[4]),
                                  )
        return sorted(self.hands, key=sorting_keys)
        


if __name__ == "__main__":

    input_path = "input.txt"
    input_lines = get_input(input_path)

    deck = Deck(input_lines)
    scores = deck.get_scores()

    # Part 1:
    part1 = sum(scores)
    print(f"Part 1: {part1}")

    # Part 2:
    # part2 = sum(scores2)
    # print(f"Part 2: {part2}")