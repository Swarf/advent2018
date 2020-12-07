

with open('data/day5') as data_file:
    passes = [line.rstrip() for line in data_file]

highest_pass_num = 0
pass_nums = []
for boarding_pass in passes:
    bin_pass = boarding_pass.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
    pass_num = int(bin_pass, 2)
    pass_nums.append(pass_num)

    if pass_num > highest_pass_num:
        highest_pass_num = pass_num

print('5a: {}'.format(highest_pass_num))

sorted_passes = sorted(pass_nums)
for index in range(len(sorted_passes) - 1):
    if sorted_passes[index + 1] == sorted_passes[index] + 2:
        print('5b: {}'.format(sorted_passes[index] + 1))
