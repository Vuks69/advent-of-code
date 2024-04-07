#!/usr/bin/python
with open("inputs/07.txt") as f:
    puzzle_input = f.read().splitlines()


def debugPrint(hands):
    from pprint import pprint

    pprint([(hand.hand, hand.handType) for hand in hands])


# index refers to power, the more the weaker
handTypes = [
    "five of a kind",  # 5
    "four of a kind",  # 4+1
    "full house",  # 3+2
    "three of a kind",  # 3+1+1
    "two pair",  # 2+2+1
    "one pair",  # 2+1+1+1
    "high card",  # 1+1+1+1+1
]


class Hand:
    hand: str
    bid: int
    handType: str

    def __init__(self, hand, bid, wildcards=False):
        self.hand = hand
        self.bid = bid
        self.handType = self.assert_type(hand, wildcards)

    def __repr__(self):
        return f"<Hand {self.hand} type:'{self.handType}' bid:{self.bid}>"

    @staticmethod
    def assert_type(hand, wildcards):
        cards = list(hand)
        uniqueCards = set(hand)
        counts = {cards.count(card) for card in uniqueCards}
        jokers = cards.count("J") if wildcards else 0
        match len(uniqueCards):
            case 1:  # 5
                return "five of a kind"
            case 2:  # 3+2  # 4+1
                if not jokers:
                    return "four of a kind" if 4 in counts else "full house"
                return "five of a kind"
            case 3:  # 3+1+1  # 2+2+1
                if not jokers:
                    return "three of a kind" if 3 in counts else "two pair"
                return "four of a kind" if 3 in counts or jokers == 2 else "full house"
            case 4:  # 2+1+1+1
                return "one pair" if not jokers else "three of a kind"
            case 5:  # 1+1+1+1+1
                return "high card" if not jokers else "one pair"


def part1(puzzle_input):
    cardLabels = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    hands = [
        Hand(hand, int(bid)) for hand, bid in [line.split() for line in puzzle_input]
    ]
    hands.sort(key=lambda x: list(map(cardLabels.index, x.hand)), reverse=True)
    hands.sort(key=lambda x: handTypes.index(x.handType), reverse=True)
    return sum([(hands.index(hand) + 1) * hand.bid for hand in hands])


def part2(puzzle_input):
    cardLabels = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    hands = [
        Hand(hand, int(bid), True)
        for hand, bid in [line.split() for line in puzzle_input]
    ]
    hands.sort(key=lambda x: list(map(cardLabels.index, x.hand)), reverse=True)
    hands.sort(key=lambda x: handTypes.index(x.handType), reverse=True)
    return sum([(hands.index(hand) + 1) * hand.bid for hand in hands])


testCases = [
    [
        "AAAAA 2",
        "22222 3",
        "AAAAK 5",
        "22223 7",
        "AAAKK 11",
        "22233 13",
        "AAAKQ 17",
        "22234 19",
        "AAKKQ 23",
        "22334 29",
        "AAKQJ 31",
        "22345 37",
        "AKQJT 41",
        "23456 43",
    ],
    ["32T3K 765", "T55J5 684", "KK677 28", "KTJJT 220", "QQQJA 483"],
    [
        "JJJJJ 5",
        "JJJJA 7",
        "JJJAA 11",
        "JJAAA 13",
        "JAAAA 17",
        "AAAAA 19",
        "JJ234 23",
        "JJ223 29",
    ],
]

for case in zip(testCases, [1343, 6440, 490]):
    assert part1(case[0]) == case[1]

print(part1(puzzle_input))
print(part2(puzzle_input))
