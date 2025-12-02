import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from base import Day

class Day02(Day):
    def solve_silver(self):
        sum_invalid = 0
        for r in self.data.split(","):
            start = r.split("-")[0]
            end = r.split("-")[1]
            
            # Remove odd numbers
            if len(start) % 2:
                start = "1"+len(start)*"0"
            if len(end) % 2:
                end = "9"*(len(end)-1)
            # print(start, end)
            for value in range(int(start), int(end)+1):
                value = str(value)
                midpoint = len(str(value))//2
                flag = True
                for i in range(midpoint):
                    if value[i] != value[midpoint+i]:
                        flag = False
                        break
                if flag:
                    sum_invalid += int(value)

        return sum_invalid

    def solve_gold(self):
        sum_invalid = 0
        for r in self.data.split(","):
            start = r.split("-")[0]
            end = r.split("-")[1]
            
            for value in range(int(start), int(end)+1):
                value = str(value)
                l = len(value)
                
                c = l
                while c > 1:
                    if l % c == 0:
                        d = l//c
                        if value == c * value[:d]:
                            sum_invalid += int(value)
                            break
                    c -=1
        return sum_invalid
    
if __name__ == "__main__":
    Day02(2).run()