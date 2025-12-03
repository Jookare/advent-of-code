import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from base import Day

class Day03(Day):
    def solve_silver(self):
        joltage = 0
        for x in self.data:
            split = [int(dig) for dig in x]
            max_digit = max(split)
            position = split.index(max_digit)
            
            if position != len(x)-1:
                # If max digit is not last
                split = split[position+1:]
                second_digit = max(split)
                largest = int(f"{max_digit}{second_digit}")
            else:
                # Max digit is last
                split = split[:-1]
                first_digit = max(split)
                largest = int(f"{first_digit}{max_digit}")
            
            joltage += largest
        return joltage

    def solve_gold(self):
        return None
    
if __name__ == "__main__":
    Day03(3).run()