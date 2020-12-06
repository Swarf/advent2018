from functools import reduce

# y, x
tree_map = []

with open('data/day3') as data_file:
    for line in data_file:
        tree_map.append([None if x == '.' else x for x in line.rstrip()])

# slope and position are y, x


def check_slope(slope):
    loc = (0, 0)
    count_trees = 0

    while loc[0] < len(tree_map):
        if tree_map[loc[0]][loc[1] % len(tree_map[loc[0]])]:
            count_trees += 1

        loc = tuple(pos + delta for pos, delta in zip(loc, slope))
    return count_trees


print("3a tree count: {}".format(check_slope((1, 3))))

slopes = [
    (1, 1),
    (1, 3),
    (1, 5),
    (1, 7),
    (2, 1),
]

tree_counts = [check_slope(x) for x in slopes]
print("3b: {}".format(reduce(lambda a, b: a * b, tree_counts)))
