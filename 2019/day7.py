from processor import Processor
from itertools import permutations

with open('data/day7') as data_file:
    codes_list = [int(x) for x in data_file.read().split(',')]

amps = [Processor(codes_list) for _ in range(5)]


def run_sequence(phase_sequence):
    signal = 0
    for amp_index, phase in enumerate(phase_sequence):
        amps[amp_index].process(phase, signal)
        signal = amps[amp_index].pop()

    return signal


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

