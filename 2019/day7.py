from processor import Processor
from itertools import permutations

with open('data/day7') as data_file:
    codes_list = [int(x) for x in data_file.read().split(',')]

p = Processor(codes_list)

p.process(1, 0)
p.reset()
p.queue_input()
p.print()

perms = permutations(range(5))


