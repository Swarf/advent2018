from processor import Processor

with open('data/day2') as day2:
    codes_list = [int(x) for x in day2.read().split(',')]

p = Processor(codes_list)
for x in range(100):
    for y in range(100):
        p.reset()
        output = p.process(x, y)
        if x == 12 and y == 2:
            print('Part 1:', output[0])
        if output[0] == 19690720:
            print('Part 2:', x * 100 + y)
            break
