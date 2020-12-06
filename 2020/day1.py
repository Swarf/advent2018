

with open('data/day1') as file:
    nums = [int(x.rstrip()) for x in file]

for index, num in enumerate(nums):
    for pair in nums[index + 1:]:
        if num + pair == 2020:
            print("day1: {}".format(num * pair))

for indexOne, one in enumerate(nums):
    for indexTwo, two in enumerate(nums[indexOne + 1:]):
        for three in nums[indexTwo + 1:]:
            if one + two + three == 2020:
                print('day1 part2: {}'.format(one * two * three))