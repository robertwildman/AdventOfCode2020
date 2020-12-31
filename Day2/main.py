def part_one():
    return read_file_excute(password_valid)


def part_two():
    return read_file_excute(position_password_valid)


def read_file_excute(func):
    with open("input.txt") as f:
        inputfile = f.read().splitlines()
        valid_passwords = 0
        for i in inputfile:
            valid_passwords += func(i)
        return valid_passwords


def password_valid(passwordstring):
    stringsections = passwordstring.split(" ")
    times = stringsections[0].split("-")
    lowest_times = times[0]
    highest_times = times[1]
    letter = stringsections[1][0]
    count = [c for c in stringsections[2]].count(letter)
    if int(lowest_times) <= count <= int(highest_times):
        return 1
    else:
        return 0


def position_password_valid(passwordstring):
    stringsections = passwordstring.split(" ")
    times = stringsections[0].split("-")
    first_pos = times[0]
    second_pos = times[1]
    letter = stringsections[1][0]
    count = [c for c in stringsections[2]]
    if (count[int(first_pos) - 1] == letter) and (count[int(second_pos) - 1] == letter):
        return 0
    elif (count[int(first_pos) - 1] != letter) and (
        count[int(second_pos) - 1] != letter
    ):
        return 0
    else:
        return 1


print("Part one Answer: " + str(part_one()))
print("Part two Answer: " + str(part_two()))
