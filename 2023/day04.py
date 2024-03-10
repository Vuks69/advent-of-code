#!/usr/bin/python
import re

with open("inputs/04.txt") as f:
    puzzle_input = f.read()


def part1(puzzle_input):
    winnings = 0
    for line in puzzle_input.split("\n"):
        w, m = line.strip().split(": ")[1].split(" | ")
        winning = [int(num) for num in w.split()]
        my = [int(num) for num in m.split()]
        exp = 0
        for n in winning:
            if n in my:
                exp += 1
        if exp > 0:
            winnings += 2 ** (exp - 1)

    return winnings


def part2(puzzle_input):
    class Card:
        card_id: int
        winning: [int]
        my: [int]
        winnings: int

        def __init__(self, id, winning, my):
            self.card_id = id
            self.winning = winning
            self.my = my

        def calculate_winnings(self):
            ret = 0
            for n in self.winning:
                if n in self.my:
                    ret += 1
            return ret

    def get_winnings(cards):
        def get_winnings_recursive(card):
            total_winnings = card.calculate_winnings()
            for offset in range(total_winnings):
                total_winnings += get_winnings_recursive(
                    cards[card.card_id + offset + 1]
                )
            return total_winnings

        return sum([get_winnings_recursive(card) + 1 for card in cards])

    cards = []
    for line in puzzle_input.split("\n"):
        card, numbers = line.strip().split(": ")
        card_id = int(card.split()[1]) - 1
        w, m = numbers.split(" | ")
        winning = [int(num) for num in w.split()]
        my = [int(num) for num in m.split()]
        cards.append(Card(card_id, winning, my))

    return get_winnings(cards)


print(part1(puzzle_input))
print(part2(puzzle_input))
