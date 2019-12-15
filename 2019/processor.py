import inspect


class Processor:
    def __init__(self, int_codes: [int]):
        self._int_codes = int_codes
        self._reset_val = int_codes.copy()
        self._op_codes = {
            1: lambda a, b: a + b,
            2: lambda a, b: a * b,
            3: self.input,
            4: self.print,
            99: lambda: False,
        }

        self._param_counts = {x: len(inspect.signature(self._op_codes[x]).parameters) for x in self._op_codes}

    def reset(self):
        self._int_codes = self._reset_val.copy()

    def print(self, a):
        print(a)
        return True

    def input(self):
        return int(input())

    def _exec_op(self, index: int = 0) -> int:
        op_code = self._int_codes[index]

        func = self._op_codes[op_code]
        params = []
        for _ in range(self._param_counts[op_code]):
            index += 1
            params.append(self._int_codes[self._int_codes[index]])

        res = func(*params)
        index += 1
        if res is False:
            return -1
        elif res is True:
            return index

        self._int_codes[self._int_codes[index]] = res
        return index + 1

    def process(self, *overrides):
        for index, val in enumerate(overrides):
            self._int_codes[index + 1] = val

        index = 0
        while index >= 0:
            index = self._exec_op(index)
        return self._int_codes


if __name__ == '__main__':
    p = Processor([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
    output = p.process()
    print(output)
