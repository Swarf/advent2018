import re

pw_pat = re.compile(r'(\d+)-(\d+)\s+([a-z]):\s+(\w+)\s*')

passwords = []
with open('data/day2') as pw_input:
    for line in pw_input:
        match = pw_pat.match(line)
        if not match:
            raise ValueError("Unmatched line: {}".format(line))

        details = {
            'range': [int(match.group(x)) for x in [1, 2]],
            'char': match.group(3),
            'pw': match.group(4)
        }

        passwords.append(details)

count_valid = 0
for details in passwords:
    if details['range'][0] <= details['pw'].count(details['char']) <= details['range'][1]:
        count_valid += 1

print("Day 2 part 1: {}".format(count_valid))

count_valid = 0
for details in passwords:
    if (details['pw'][details['range'][0] - 1] == details['char']) ^ (details['pw'][details['range'][1] - 1] == details['char']):
        count_valid += 1

print("Day 2 part 2: {}".format(count_valid))
