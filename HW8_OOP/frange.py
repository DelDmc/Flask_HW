import math


class frange:
    def __init__(self, start, stop, step=1.0):
        self._start = start
        self._stop = stop
        self._step = step
        self.qty_steps = int(math.ceil((self._stop - self._start) / float(self._step)))
        self.step_counter = 0

    def __next__(self):
        if self.qty_steps > 1:
            result = self._start + self._step * self.step_counter
            self.step_counter += 1
            if self.step_counter > self.qty_steps:
                raise StopIteration('ffff')
            return result
        elif self.qty_steps == 1:
            return self._start
        else:
            raise StopIteration('ffff')

    def __iter__(self):
        return self


assert(list(frange(0, 5)) == [0, 1, 2, 3, 4])
assert(list(frange(2, 5)) == [2, 3, 4])
assert(list(frange(2, 10, 2)) == [2, 4, 6, 8])
assert(list(frange(10, 2, -2)) == [10, 8, 6, 4])
assert(list(frange(2, 5.5, 1.5)) == [2, 3.5, 5])
assert(list(frange(1, 5)) == [1, 2, 3, 4])
assert(list(frange(0, 5)) == [0, 1, 2, 3, 4])
assert(list(frange(0, 0)) == [])
assert(list(frange(100, 0)) == [])

print('SUCCESS!')