from processor import Processor

with open('data/day2') as day2:
    codes_list = [int(x) for x in day2.read().split(',')]


def add(a, b):
    return a + b


def mult(a, b):
    return a * b


def exec_op(codes, index=0):
    op_code = codes[index]
    if op_code == 99:
        return False
    elif op_code == 1:
        func = add
    elif op_code == 2:
        func = mult
    else:
        raise ValueError('invalid opcode ' + op_code)

    res = func(codes[codes[index + 1]], codes[codes[index + 2]])
    codes[codes[index + 3]] = res
    return True


def process(codes):
    running = True
    index = 0
    while running:
        running = exec_op(codes, index)
        index += 4
    return codes


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
