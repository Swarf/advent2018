# day3


with open('data/day3') as data_file:
    paths = [[(x[0], int(x[1:])) for x in line.split(',')] for line in data_file]

directions = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1),
}

# paths[0] = [(x[0], int(x[1:])) for x in 'R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(',')]
# paths[1] = [(x[0], int(x[1:])) for x in 'U62,R66,U55,R34,D71,R55,D58,R83'.split(',')]
# paths[0] = [(x[0], int(x[1:])) for x in 'R8,U5,L5,D3'.split(',')]
# paths[1] = [(x[0], int(x[1:])) for x in 'U7,R6,D4,L4'.split(',')]

points = {}
closest_intersect = None
fastest_intersect = None
for path_index, path in enumerate(paths):
    marker = 0, 0
    steps = 0
    for move in path:
        direction = directions[move[0]]
        for _ in range(move[1]):
            steps += 1
            marker = (marker[0] + direction[0], marker[1] + direction[1])
            val_check = points.setdefault(marker, (path_index, steps))
            if path_index != val_check[0]:
                dist = abs(marker[0]) + abs(marker[1])
                time = steps + val_check[1]
                if closest_intersect is None or dist < closest_intersect:
                    closest_intersect = dist
                if fastest_intersect is None or time < fastest_intersect:
                    fastest_intersect = time

print(closest_intersect)
print(fastest_intersect)
