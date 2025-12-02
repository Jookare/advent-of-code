import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from base import Day

class Day01(Day):
    def solve_silver(self):
        point = 50
        counter = 0

        for move in self.data:
            side = move[0]
            rot = int(move[1:])

            if side == "L":
                end_raw = point - rot
            else:
                end_raw = point + rot

            point = end_raw % 100
            if point == 0:
                counter += 1

        return counter

    def solve_gold(self):
        point = 50
        counter = 0

        for move in self.data:
            side = move[0]
            rot = int(move[1:])

            if side == "L":
                end_raw = point - rot
                if point == 0:
                    counter += rot // 100
                else:
                    counter += (100 - end_raw) // 100
            else:
                # Counter = (sp + rot) // 100
                end_raw = point + rot
                if point == 0:
                    counter += rot // 100
                else:
                    counter += end_raw // 100

            point = end_raw % 100

        return counter
    
if __name__ == "__main__":
    Day01(1).run()