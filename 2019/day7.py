from processor import Processor
from itertools import permutations

with open('data/day7') as data_file:
    codes_list = [int(x) for x in data_file.read().split(',')]

_ = codes_list
codes_list = [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26, 27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5]

amps = [Processor(codes_list) for _ in range(5)]


def run_sequence(phase_sequence):
    signal = 0
    for amp_index, phase in enumerate(phase_sequence):
        amps[amp_index].process(phase, signal)
        signal = amps[amp_index].pop()
        amps[amp_index].reset()
    return signal


test = run_sequence([9, 8, 7, 6, 5])
exit(0)

perms = permutations(range(5))
highest_signal = 0
best_sequence = None

for sequence in perms:
    potential = run_sequence(sequence)
    if potential > highest_signal:
        highest_signal = potential
        best_sequence = sequence

print(highest_signal)
print(best_sequence)
