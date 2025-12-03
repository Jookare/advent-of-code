import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from base import Day

class Day03(Day):
    def solve_silver(self):
        joltage = 0
        for x in self.data:
            split = list(map(int, x))
            joltage += self.find_max_joltage(split, 2)
        return joltage

    def solve_gold(self):
        joltage = 0
        for x in self.data:
            split = list(map(int, x))
            joltage += self.find_max_joltage(split, 12)
        return joltage

    def find_max_joltage(self, split, n):
        start_idx = 0
        index_list = []
        # Find n digits
        for i in range(1,n+1):
            # First digit has to be atleast n away from the end
            end_idx = len(split)-(n-i)

            # Find maximum from the interval
            max_num = max(split[start_idx:end_idx])

            # Find index from the interval
            max_idx = split.index(max_num, start_idx, end_idx)
            index_list.append(max_idx)
            start_idx = max_idx+1
        
        values = [str(split[id]) for id in (index_list)]
        return int("".join(values))
    
if __name__ == "__main__":
    Day03(3).run()