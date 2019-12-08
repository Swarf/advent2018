from string import ascii_lowercase

with open('data/day5') as data:
    input_list = list([line.strip() for line in data][0])


# input_list = ['a', 'A', 'a', 'b', 'C', 'c', 'B', 'a', 'B']


def react(polymer):
    index = 1
    while index < len(polymer):
        if abs(ord(polymer[index]) - ord(polymer[index - 1])) == 32:
            polymer[index - 1: index + 1] = []
            index = max(index - 1, 1)
        else:
            index += 1

    return polymer


print('reduce all:', len(react(list(input_list))))
# print(input_list)

smallest_len = None
smallest_seq = None

for letter in ascii_lowercase:
    one_less = [x for x in input_list if x != letter and x != chr(ord(letter) - 32)]
    size = len(react(one_less))
    if smallest_len is None or size < smallest_len:
        smallest_len = size
        smallest_seq = letter


print(smallest_seq, smallest_len)


