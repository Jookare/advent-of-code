import sys
from pathlib import Path
from collections import defaultdict

sys.path.append(str(Path(__file__).resolve().parent.parent))

from base import Day
from functools import reduce

class Day07(Day):
    def solve_silver(self):
        start_point = self.data[0].index("S")
        map = {".": 0, "^": 1}
        diagram = [[map[ch] for ch in row] for row in self.data[1:]]


        path = []
        counter = 0
        for row in diagram:
            # if no splinters do not iterate
            if sum(row)>0:
                for col_id, ch in enumerate(row):
                    # First splitter
                    if ch == 1 and len(path) == 0 and col_id == start_point:
                        path += [col_id-1, col_id+1]
                        counter += 1
                    # Following splitters
                    elif ch == 1 and col_id in path:
                        path.remove(col_id)
                        path += [col_id-1, col_id+1]
                        counter += 1
                    
                path = list(set(path))
                
        return counter

    def solve_gold(self):
        start_point = self.data[0].index("S")
        map = {".": 0, "^": 1, "S": 0}
        diagram = [[map[ch] for ch in row] for row in self.data]

        # Create counter for columns
        counter = {start_point: 1,}

        for row in diagram:
            # Find all indices of splitters
            index = {c for c in counter if row[c] == 1}

            # Loop through
            for i in index:
                # Add both left and right if not in counter
                # otherwise add from the current path
                if i-1 not in counter:
                    counter[i-1] = counter[i]
                else:
                    counter[i-1] += counter[i]
                
                if i+1 not in counter:
                    counter[i+1] = counter[i]
                else:
                    counter[i+1] += counter[i]

                # Reset current column value
                del counter[i]
                
        return sum(counter.values())

if __name__ == "__main__":
    Day07(7).run()
