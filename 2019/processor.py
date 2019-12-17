import inspect


class Processor:
    def __init__(self, int_codes: [int]):
        self._int_codes = int_codes
        self._reset_val = int_codes.copy()
        self._op_codes = {
            1: lambda a, b: a + b,
            2: lambda a, b: a * b,
            3: self.input,
            4: self.output,
            5: lambda a, b: self.move(bool(a), b),
            6: lambda a, b: self.move(not a, b),
            7: lambda a, b: int(a < b),
            8: lambda a, b: int(a == b),
            99: lambda: False,
        }
        self.index = 0
        self._input_queue = []
        self._output_buffer = []
        self._param_counts = {x: len(inspect.signature(self._op_codes[x]).parameters) for x in self._op_codes}

    def reset(self, *overrides):
        self._int_codes = self._reset_val.copy()
        self.index = 0
        for index, val in enumerate(overrides):
            self._int_codes[index + 1] = val
        self._input_queue.clear()

    def output(self, a):
        self._output_buffer.append(a)
        return True

    def input(self):
        return self._input_queue.pop() if self._input_queue else int(input('number: '))

    def move(self, test, position):
        if test:
            self.index = position
        return True

    def _exec_op(self):
        instruction_code = self._int_codes[self.index]
        op_code = instruction_code % 100

        try:
            func = self._op_codes[op_code]
        except KeyError:
            print("ERROR! Bad op code: {}".format(op_code))
            op_code = 99
            func = self._op_codes[op_code]

        params = []
        for i in range(self._param_counts[op_code]):
            self.index += 1
            param_mode = instruction_code // 10 ** (i + 2) % 10
            int_code = self._int_codes[self.index]
            params.append(int_code if param_mode else self._int_codes[int_code])

        self.index += 1
        res = func(*params)
        if res is False:
            self.index = -1
            return
        elif res is True:
            return

        self._int_codes[self._int_codes[self.index]] = res
        self.index += 1

    def process(self, *inputs):
        self._input_queue.extend(inputs)
        while self.index >= 0:
            self._exec_op()
        return self._int_codes

    def queue_input(self):
        self._input_queue.append(self._input_queue.pop(0))

    def print(self):
        for output in self._output_buffer:
            print(output)
        self._output_buffer.clear()


if __name__ == '__main__':
    p = Processor([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
    result = p.process()
    print(result)
