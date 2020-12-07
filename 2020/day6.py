

groups = []
excl_groups = []

with open('data/day6') as data_file:
    group = []
    groups.append(group)

    for line in [x.rstrip() for x in data_file]:
        if not line:
            group = []
            groups.append(group)
            continue

        group.append(set(line))

union_yes = 0
intersect_yes = 0
for group in groups:
    group_union = set()
    for answer in group:
        group_union.update(answer)
    union_yes += len(group_union)

    group_intersect = group[0]
    for answer in group[1:]:
        group_intersect = group_intersect.intersection(answer)
    intersect_yes += len(group_intersect)


print('6a: {}'.format(union_yes))
print('6b: {}'.format(intersect_yes))

