
from collections import defaultdict

with open('data/day2a') as data:
    input_list = [line.rstrip() for line in data]


def check_count(values, target):
    for value in values:
        yield value == target


counts = defaultdict(int)
pair = 0
triplet = 0

for foo in input_list:
    for letter in foo:
        counts[letter] += 1

    if any(check_count(counts.values(), 2)):
        pair += 1

    if any(check_count(counts.values(), 3)):
        triplet += 1

    counts.clear()

print(pair * triplet)


for index, foo in enumerate(input_list):
    for bar in input_list[index + 1:]:
        diff_count = 0
        same = ''
        for a, b in zip(foo, bar):
            if a == b:
                same += a
            else:
                diff_count += 1
                if diff_count > 1:
                    break

        if diff_count <= 1:
            print(same)

