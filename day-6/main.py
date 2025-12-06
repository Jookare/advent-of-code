import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from base import Day
from functools import reduce

class Day06(Day):
    def solve_silver(self):
        # Split input into symbols and numbers
        inputs_grid = list(map(str.split, self.data))
        symbols = inputs_grid[-1]
        numbers = [[int(x) for x in row] for row in inputs_grid[:-1]]

        # Init sum array 1 for multiplication and 0 for sum
        sum_array = [int(sym == "*") for sym in symbols]
        for row in numbers:
            for i, x in enumerate(row):
                if symbols[i] == "*":
                    sum_array[i] *= x
                else:
                    sum_array[i] += x

        # Compute sum
        res = reduce(self.add, sum_array)
        return res

    def solve_gold(self):
        # Find symbols
        symbols = list(map(str.split, self.data))[-1]

        # Numbers: array of size [W x H]
        print(len(list(self.data[0])), len(list(self.data[1])), len(list(self.data[2])), len(list(self.data[3])))

        numbers = [[] for j in range(len(self.data[0]))]

        # Create transposed version of the original data
        for row_id, arr in enumerate(self.data[:-1]):
            for col_id, ch in enumerate(arr):
                if ch != ' ':
                    numbers[col_id] += ch

        cache = []
        total = []
        operation_id = 0
        # Go through the transposed array
        for i, arr in enumerate(numbers):

            # Join the numbers
            joined_arr = "".join(arr)

            # if not empty row add to cache
            if len(joined_arr) > 0:
                cache.append(int(joined_arr))

            # Else do operation using cached numbers
            if len(joined_arr) == 0 or i == len(numbers)-1:
                # Do operation based on symbol
                if symbols[operation_id] == "*":
                    total.append(reduce(self.mul, cache))
                else:
                    total.append(reduce(self.add, cache))
                operation_id += 1
                cache = []
                
        return reduce(self.add, total)

    def add(self, x, y):
        return x + y
    
    def mul(self, x, y):
        return x * y


if __name__ == "__main__":
    Day06(6).run()
