import re

passports = []
fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}
num_fields = {'byr', 'iyr', 'eyr'}

with open('data/day4') as data_file:
    passport = {}
    for line in data_file:
        line = line.rstrip()
        if not line:
            passports.append(passport)
            passport = {}
            continue

        for pair in line.split(' '):
            key, value = pair.split(':')
            if key in num_fields:
                value = int(value)
            if key not in fields:
                raise ValueError("Invalid key: {}".format(key))

            passport[key] = value

    passports.append(passport)

height_pat = re.compile(r'(\d+)(in|cm)')


def check_height(maybe_height):
    match = height_pat.fullmatch(maybe_height)
    if match:
        height_val = int(match.group(1))
        if match.group(2) == 'cm':
            return 150 <= height_val <= 193
        else:
            return 59 <= height_val <= 76
    return False


color_pat = re.compile(r'#[a-f0-9]{6}')
pid_pat = re.compile(r'[0-9]{9}')
eye_colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
validators = {
    'byr': lambda x: 1920 <= x <= 2002,
    'iyr': lambda x: 2010 <= x <= 2020,
    'eyr': lambda x: 2020 <= x <= 2030,
    'hcl': lambda x: color_pat.fullmatch(x),
    'hgt': check_height,
    'ecl': lambda x: x in eye_colors,
    'pid': lambda x: pid_pat.fullmatch(x),
    'cid': lambda x: True,
}

passports_with_fields = []
for passport in passports:
    missing = fields - passport.keys()
    if missing == set() or missing == {'cid'}:
        passports_with_fields.append(passport)

print('4a: {}'.format(len(passports_with_fields)))

count_valid = 0
for passport in passports_with_fields:
    passing = True
    for key, value in passport.items():
        if not validators[key](value):
            passing = False
            break

    if passing:
        count_valid += 1

print('4b: {}'.format(count_valid))
