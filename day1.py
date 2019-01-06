

with open('data/day1b') as data:
    input_list = [int(line) for line in data]

start = 0
uniq = {start}


def loop_once(cur):
    for num in input_list:
        cur += num
        if cur in uniq:
            return cur
        uniq.add(cur)
    return loop_once(cur)


print(loop_once(start))
