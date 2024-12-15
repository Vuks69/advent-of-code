#!/usr/bin/python
with open("inputs/05.txt") as f:
    puzzle_input = f.read().splitlines()

example = [
    "47|53",
    "97|13",
    "97|61",
    "97|47",
    "75|29",
    "61|13",
    "75|53",
    "29|13",
    "97|29",
    "53|29",
    "61|53",
    "97|53",
    "61|29",
    "47|13",
    "75|47",
    "97|75",
    "47|61",
    "75|61",
    "47|29",
    "75|13",
    "53|13",
    "",
    "75,47,61,53,29",
    "97,61,53,29,13",
    "75,29,13",
    "75,97,47,61,53",
    "61,13,29",
    "97,13,75,29,47",
]


def verify_update(update, dependencies):
    printed = set()
    for page in update:
        if page in dependencies:  # if page has dependencies
            for dep in dependencies[page]:
                if dep in update and dep not in printed:
                    # if dependency is in update and wasn't already printed, bail
                    return False
        printed.add(page)
    return True


def fix_update(update: list, dependencies):
    printed = set()
    i = 0
    while i < len(update):
        if update[i] in dependencies:  # if page has dependencies
            for dep in dependencies[update[i]]:
                if dep in update and dep not in printed:
                    # found a page that needs to be fixed
                    # can i just swap them?
                    idx = update.index(dep)
                    update[i], update[idx] = (
                        update[idx],
                        update[i],
                    )
                    # why is it not swapping
                    # but now i need to check if the order is correct... recursion?
                    # or just go back to 0, resetting everything?
                    i = 0
                    printed = set()
                    break
            else:
                # if page was okay - go on
                printed.add(update[i])
                i += 1
        else:
            printed.add(update[i])
            i += 1
    return update


def build_dependency_tree(rules):
    dependencies = {}
    for rule in rules:
        # rule[1] depends on rule[0]
        if rule[1] in dependencies:
            dependencies[rule[1]].append(rule[0])
        else:
            dependencies[rule[1]] = [rule[0]]
    return dependencies


def part1(puzzle_input: list[str]):
    j = puzzle_input.index("")
    rules = [[int(x) for x in i.split("|")] for i in puzzle_input[:j]]
    updates = [[int(x) for x in i.split(",")] for i in puzzle_input[j + 1 :]]
    dependencies = build_dependency_tree(rules)
    return sum(
        [
            update[len(update) // 2]
            for update in updates
            if verify_update(update, dependencies)
        ]
    )


def part2(puzzle_input):
    j = puzzle_input.index("")
    rules = [[int(x) for x in i.split("|")] for i in puzzle_input[:j]]
    updates = [[int(x) for x in i.split(",")] for i in puzzle_input[j + 1 :]]
    dependencies = build_dependency_tree(rules)
    bad_updates = [
        update for update in updates if not verify_update(update, dependencies)
    ]
    return sum(
        [
            fixed[len(fixed) // 2]
            for fixed in [fix_update(update, dependencies) for update in bad_updates]
        ]
    )


# print(part1(example))
print(part1(puzzle_input))
# print(part2(example))
print(part2(puzzle_input))
