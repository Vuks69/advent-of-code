#!/usr/bin/python
import re
from itertools import cycle
from math import lcm

with open("inputs/08.txt") as f:
    puzzle_input = f.read().splitlines()


def part1(puzzle_input):
    moves = cycle(puzzle_input[0])
    # nodes = {
    #     "NNN": {"L": "TNT", "R": "XDJ"},
    # }
    nodes = {
        node: {"L": left, "R": right}
        for line in puzzle_input[2:]
        for (node, left, right) in re.findall(
            r"([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)", line
        )
    }  # what the fuck
    steps = 0
    current_node = "AAA"
    while current_node != "ZZZ":
        current_node = nodes[current_node][next(moves)]
        steps += 1
    return steps


def part2(puzzle_input):
    # nodes = {
    #     "NNN": {"L": "TNT", "R": "XDJ"},
    # }
    nodes = {
        node: {"L": left, "R": right}
        for line in puzzle_input[2:]
        for (node, left, right) in re.findall(
            r"([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)", line
        )
    }  # what the fuck
    steps = 0
    starting_nodes = [node for node in nodes.keys() if node.endswith("A")]

    def get_loop_length(
        node,
    ):
        # all ghosts end up on exactly one ..Z node, then loop - LCM
        moves = cycle(puzzle_input[0])
        steps = 0
        while not node.endswith("Z"):
            node = nodes[node][next(moves)]
            steps += 1
        return steps

    loops = map(get_loop_length, starting_nodes)
    return lcm(*loops)


print(part1(puzzle_input))
print(part2(puzzle_input))
