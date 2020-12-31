def part_one():
    return tree_finder(3, 1)


def part_two():
    trees_hit = tree_finder(1, 1)
    trees_hit = trees_hit * tree_finder(3, 1)
    trees_hit = trees_hit * tree_finder(5, 1)
    trees_hit = trees_hit * tree_finder(7, 1)
    trees_hit = trees_hit * tree_finder(1, 2)
    return trees_hit


def tree_finder(addx, addy):
    with open("input.txt") as f:
        skimap = f.read().splitlines()
        currentcords_x = 0
        currentcords_y = 0
        trees_hit = 0
        while True:
            currentcords_x += addx
            currentcords_y += addy
            if currentcords_y >= len(skimap):
                break
            if currentcords_x >= len(skimap[0]):
                currentcords_x = currentcords_x - len(skimap[0])
            if skimap[currentcords_y][currentcords_x] == "#":
                trees_hit += 1
        return trees_hit


print("Part one answer: " + str(part_one()))
print("Part two answer: " + str(part_two()))
