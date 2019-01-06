import re
from collections import namedtuple, defaultdict

Square = namedtuple('Square', ['id', 'row', 'col', 'width', 'height'])

with open('data/day3a') as data:
    pat = re.compile(r'[^0-9]+')
    input_list = [pat.split(line[1:].strip()) for line in data]
    claim_list = [Square(*[int(x) for x in claim]) for claim in input_list]

# print(*claims[0:5], sep='\n')

fabric = defaultdict(set)
claims = defaultdict(int)

for square in claim_list:
    for x in range(square.width):
        for y in range(square.height):
            key = (square.row + x, square.col + y)
            fabric[key].add(square.id)
            for claim_id in fabric[key]:
                claims[claim_id] = max(len(fabric[key]) - 1, claims[claim_id])

print(sum([len(claimers) > 1 for claimers in fabric.values()]))

for claim_id, overlaps in claims.items():
    if overlaps == 0:
        print(claim_id)
