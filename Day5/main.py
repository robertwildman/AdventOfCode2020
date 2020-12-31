def part_one():
    with open("input.txt") as f:
        highest_seat = 0
        boarding_passes = f.read().splitlines()
        for passes in boarding_passes:
            if string_to_seatid(passes) > highest_seat:
                highest_seat = string_to_seatid(passes)
        return highest_seat


def part_two():
    with open("input.txt") as f:
        highest_seat = 0
        seats = []
        boarding_passes = f.read().splitlines()
        for passes in boarding_passes:
            seats.append(string_to_seatid(passes))
            if string_to_seatid(passes) > highest_seat:
                highest_seat = string_to_seatid(passes)
        seats.sort()
        for i in range(1, len(seats)):
            if not (seats[i] - 1) in seats:
                return seats[i] - 1


def string_to_seatid(input_string):
    row = [0, 127]
    column = [0, 7]
    for x in range(0, 7):
        row = group_seating(input_string[x], row)
    for x in range(7, 10):
        column = column_seating(input_string[x], column)
    return row[0] * 8 + column[0]


def group_seating(pos, rows):
    mid = (rows[1] + rows[0]) // 2
    if pos == "F":
        rows[1] = mid
    else:
        rows[0] = mid + 1
    return rows


def column_seating(pos, rows):
    mid = (rows[1] + rows[0]) // 2
    if pos == "L":
        rows[1] = mid
    else:
        rows[0] = mid + 1
    return rows


# Code to run
print("Part one answer: " + str(part_one()))
print("Part two answer: " + str(part_two()))
