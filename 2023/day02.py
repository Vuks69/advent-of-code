#!/usr/bin/python
import re

with open("inputs/02.txt") as f:
    puzzle_input = f.read()


def part1(puzzle_input):
    max_cubes = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    total = 0
    for line in puzzle_input.split("\n"):
        game_possible = True
        game, shows = line.strip().split(": ")
        game_id = int(game.removeprefix("Game "))
        for show in shows.split("; "):
            for cubes in show.split(", "):
                amount, color = cubes.split(" ")
                if int(amount) > max_cubes[color]:
                    game_possible = False
        if game_possible:
            total += game_id

    return total


def part2(puzzle_input):
    cubes_regex = re.compile(r"(\d+) (red|green|blue)")
    total = 0
    for line in puzzle_input.split("\n"):
        amounts = {"red": [], "green": [], "blue": []}
        for amount, color in re.findall(cubes_regex, line):
            amounts[color].append(int(amount))
        total += max(amounts["red"]) * max(amounts["green"]) * max(amounts["blue"])

    return total


print(part1(puzzle_input))
print(part2(puzzle_input))
