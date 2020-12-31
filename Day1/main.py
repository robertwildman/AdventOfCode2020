def part_one():
    with open("input.txt") as f:
        expenses = f.read().splitlines()
        expenses = [int(e) for e in expenses]
        for exp in expenses:
            for inexp in expenses:
                if exp + inexp == 2020:
                    return exp * inexp


def part_two():
    with open("input.txt") as f:
        expenses = f.read().splitlines()
        expenses = [int(e) for e in expenses]
        for exp in expenses:
            for exp2 in expenses:
                for exp3 in expenses:
                    if exp + exp2 + exp3 == 2020:
                        return exp * exp2 * exp3


# Code to run
print("Part one answer: " + str(part_one()))
print("Part two answer: " + str(part_two()))
