from processor import Processor

with open('data/day5') as data_file:
    codes_list = [int(x) for x in data_file.read().split(',')]

p = Processor(codes_list)
output = p.process()

p.reset()
