#!/usr/bin/python
with open("inputs/04.txt") as f:
    puzzle_input = f.read().splitlines()

# Find # of "XMAS", in every direction + diagonally
# There's 18 in example below.
example = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX",
]

# Find two "MAS" in the shape of an X
# There's 9 in example below
example2 = [
    ".M.S......",
    "..A..MSMS.",
    ".M.S.MAA..",
    "..A.ASMSM.",
    ".M.S.M....",
    "..........",
    "S.S.S.S.S.",
    ".A.A.A.A..",
    "M.M.M.M.M.",
    "..........",
]


import re


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, o):
        return Point(self.x + o.x, self.y + o.y)


directions = {
    "N": Point(0, -1),
    "NE": Point(1, -1),
    "E": Point(1, 0),
    "SE": Point(1, 1),
    "S": Point(0, 1),
    "SW": Point(-1, 1),
    "W": Point(-1, 0),
    "NW": Point(-1, -1),
}


# Y = row
# X = column
def p1_find_next_letter(
    puzzle_array: list[list[bytes]], letter: int, position: (int, int), direction: str
):
    word_to_find = "XMAS"
    next_pos = position + directions[direction]
    next_letter = letter + 1
    debug_current_letter_world = puzzle_array[position.y][position.x]
    debug_to_find = word_to_find[next_letter]
    if next_pos.x in range(len(puzzle_array[0])) and next_pos.y in range(
        len(puzzle_array)
    ):  # if we're looking within the array
        debug_next_letter_world = puzzle_array[next_pos.y][next_pos.x]
        if (
            puzzle_array[next_pos.y][next_pos.x] == word_to_find[next_letter]
        ):  # if the next position contains the next letter
            if next_letter == len(word_to_find) - 1:  # if that was the last letter
                return True
            return p1_find_next_letter(puzzle_array, next_letter, next_pos, direction)
    return False


def p2_find_x(puzzle_array, position):
    pass


def part1(puzzle_input):
    pattern = re.compile("X")

    starting_positions = [
        [Point(iter.start(), i) for iter in re.finditer(pattern, puzzle_input[i])]
        for i in range(len(puzzle_input))
    ]

    found = 0
    for line in starting_positions:
        for pos in line:
            for dir in directions.keys():
                if p1_find_next_letter(puzzle_input, 0, pos, dir):
                    found += 1
    return found


def part2(puzzle_input):
    pattern = re.compile("A")

    starting_positions = [
        [Point(iter.start(), i) for iter in re.finditer(pattern, puzzle_input[i])]
        for i in range(len(puzzle_input))
    ]

    found = 0
    for line in starting_positions[1:-1]:
        for pos in line:
            if pos.x != 0 and pos.x != len(line) - 1:
                if p2_find_x(puzzle_input, pos):
                    found += 1
    return found


print(part1(puzzle_input))
assert part1(example) == 18
print(part2(puzzle_input))
assert part2(example) == 9
assert part2(example2) == 9
