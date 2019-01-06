from operator import itemgetter

with open('data/day6') as data:
    input_list = [tuple(map(int, line.split(', '))) for line in data]

# input_list = [
#     (1, 1),
#     (1, 6),
#     (8, 3),
#     (3, 4),
#     (5, 5),
#     (8, 9),
# ]

by_x = sorted(input_list, key=itemgetter(0))
by_y = sorted(input_list, key=itemgetter(1))

x_range = [point[0] for point in by_x[0::len(by_x) - 1]]
y_range = [point[1] for point in by_y[0::len(by_y) - 1]]
x_range[1] += 1
y_range[1] += 1


# directions = [(x, y) for x in range(-1, 2) for y in range(-1, 2) if x or y]  # 8 directions
# directions = [(x, y) for x in range(-1, 2) for y in range(-1, 2) if x or y]  # 4 directions


def perimeter(dist):
    upper = [(x, dist - abs(x)) for x in range(-dist, dist)]
    lower = [(x, abs(x) - dist) for x in range(dist, -dist, -1)]

    return upper + lower


locations = {loc: loc for loc in input_list}
point_areas = {loc: 1 for loc in input_list}
area_size = (x_range[1] - x_range[0]) * (y_range[1] - y_range[0])  # Total number of locations
infinite_adjacent = set()
edge = {}

growth = 0

while len(locations) < area_size:
    growth += 1
    deltas = perimeter(growth)
    additions = {}

    # Grow the perimeter
    # For each point, check all the new perimeter locations and fill up the new additions
    # Skip any locations already claimed by a point.
    # If two points would claim a location in this same perimeter expansion, no point claims it
    for point in input_list:
        for delta in deltas:
            check_loc = tuple(map(sum, zip(point, delta)))  # Add the delta to the point
            if x_range[0] <= check_loc[0] < x_range[1] and y_range[0] <= check_loc[1] < y_range[1]:
                if check_loc not in locations:
                    if check_loc in additions:
                        if additions[check_loc] in point_areas:
                            point_areas[additions[check_loc]] -= 1
                        additions[check_loc] = None
                    else:
                        additions[check_loc] = point
                        if point in point_areas:
                            point_areas[point] += 1
            elif check_loc not in edge:  # TODO needs optimization to also exclude anything +1 outside valid range
                edge[check_loc] = point
                if point not in infinite_adjacent:
                    infinite_adjacent.add(point)
                    del point_areas[point]

    locations.update(additions)

back_map = {
    (1, 1): 'A',
    (1, 6): 'B',
    (8, 3): 'C',
    (3, 4): 'D',
    (5, 5): 'E',
    (8, 9): 'F',
}

# print(x_range)
# print(y_range)


def print_grid():
    for y in range(*y_range):
        row_chars = []
        for x in range(*x_range):
            loc = x, y
            if loc not in locations:
                row_chars.append('?')
                continue
            owner = locations[loc]
            del locations[loc]
            letter = '.' if owner is None else back_map[owner]
            if loc != owner:
                letter = letter.lower()

            row_chars.append(letter)
        print(''.join(row_chars))


largest_point_area = max(point_areas, key=point_areas.get)
print('largest point area', largest_point_area, point_areas[largest_point_area])

limit = 10000
within_limit = 0
for row in range(*y_range):
    for col in range(*x_range):
        dist_sum = 0
        for point in input_list:
            dist_sum += abs(col - point[0])
            dist_sum += abs(row - point[1])
            if dist_sum >= limit:
                break

        if dist_sum < limit:
            within_limit += 1

print('area within {}: {}'.format(limit, within_limit))
