# Advent of Code 2023
# https://adventofcode.com/2023/day/4

import os
# Change working directory to where this script is saved
os.chdir(os.path.dirname(__file__))

# --- End of header and initialization -----------------

class Card():

    def __init__(self, txt_description):
        self.id, self.num_win, self.num_own = self.parse_input(txt_description)
        self.count = 1

    def parse_input(self, txt_description):
        id_part, num_part = txt_description.split(":")
        _, id = id_part.split()
        id = int(id)
        num_win, num_own = num_part.split("|")
        # split() considers multiple whitespace characters as a single separator
        num_win = num_win.strip().split()
        num_own = num_own.strip().split()
        num_win = [int(n) for n in num_win]
        num_own = [int(n) for n in num_own]
        return id, num_win, num_own
    
    def get_number_of_winning(self):
        winning = set(self.num_win).intersection(set(self.num_own))
        return len(winning)
    
    def get_score(self):
        n_winning = self.get_number_of_winning()
        score = 2**(n_winning-1) if n_winning > 0 else 0
        return score
    
    def __repr__(self):
        return f"Card {self.id}"


def get_input(input_path):
    with open(input_path, "r") as file:
        return [line.strip() for line in file]


if __name__ == "__main__":

    input_path = "input.txt"
    txt_lines = get_input(input_path)

    cards = [Card(txt_description=line) for line in txt_lines]

    # Part 1:
    scores = [card.get_score() for card in cards]
    part1 = sum(scores)
    print(f"Part 1: {part1}")

    # Part 2:
    for ind_current, card in enumerate(cards):
        n_winning = card.get_number_of_winning()        
        indices_to_copy = range(ind_current+1, ind_current+1+n_winning)
        for i_copy in indices_to_copy:
            cards[i_copy].count += cards[ind_current].count
    
    # for card in cards:
    #     print(f"Card {card.id}: {card.count}")

    card_counts = [card.count for card in cards]
    part2 = sum(card_counts)
    print(f"Part 2: {part2}")



    '''
    # Part 2: Original "literal" representation - too computationally demanding

    import copy

    def find_card_last_index(cards, id_searched):
        card_ids = [card.id for card in cards]
        # Reverse list to find last index occurrence
        idx_rev = card_ids[::-1].index(id_searched)
        return len(cards) - idx_rev - 1

    i = 0
    cards2 = copy.deepcopy(cards)
    while i < len(cards2):
        n_winning = cards2[i].get_number_of_winning()
        id_current = cards2[i].id
        ids_to_copy = range(id_current+1, id_current+n_winning+1)
        for id in ids_to_copy:
            index_insertion = find_card_last_index(cards2, id)
            card_copy = copy.deepcopy(cards2[index_insertion])
            cards2.insert(index_insertion+1, card_copy)
        i += 1
    '''