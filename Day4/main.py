import re


def part_one():
    with open("input.txt") as f:
        inputfile = f.read().splitlines()
        passportkeys = {}
        valid_passports = 0
        for line in inputfile:
            if len(line) == 0:
                valid_passports += checkpassport(passportkeys.keys())
                passportkeys = {}
            else:
                key_pairs = line.split(" ")
                for keys in key_pairs:
                    keysplit = keys.split(":")
                    passportkeys[keysplit[0]] = keysplit[1]
        return valid_passports


def checkpassport(keys):
    required_field = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    result = all(elem in keys for elem in required_field)
    if result:
        return 1
    else:
        return 0


def part_two():
    with open("input.txt") as f:
        inputfile = f.read().splitlines()
        passportfields = {}
        valid_passports = 0
        for line in inputfile:
            if len(line) == 0:
                valid_passports += checkpassport_p2(passportfields)
                passportfields = {}
            else:
                key_pairs = line.split(" ")
                for keys in key_pairs:
                    keysplit = keys.split(":")
                    passportfields[keysplit[0]] = keysplit[1]
        return valid_passports


def checkpassport_p2(fields):
    required_field = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    result = all(elem in fields.keys() for elem in required_field)
    if result:
        if check_valid_fields(fields):
            return 1
        else:
            return 0
    else:
        return 0


def check_valid_fields(fields):
    height_string = fields.get("hgt")
    eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if not 1920 <= int(fields.get("byr")) <= 2002:
        return False
    elif not 2010 <= int(fields.get("iyr")) <= 2020:
        return False
    elif not 2020 <= int(fields.get("eyr")) <= 2030:
        return False
    elif not ("cm" in height_string or "in" in height_string):
        print(height_string)
        return False
    elif not any(color in fields.get("ecl") for color in eye_colors):
        return False
    elif not re.search(r"^[0-9]{9}$", fields.get("pid")):
        return False
    elif not re.search(r"^#(?:[0-9a-fA-F]{3}){1,2}$", fields.get("hcl")):
        return False

    if "cm" in height_string:
        height = int(height_string.replace("cm", ""))
        if 150 <= height <= 193:
            return True
        else:
            return False
    elif "in" in height_string:
        height = int(height_string.replace("in", ""))
        if 59 <= height <= 76:
            return True
        else:
            return False


# Code to run
print("Part one answer: " + str(part_one()))
print("Part two answer: " + str(part_two()))
