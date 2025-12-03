import time
from pathlib import Path

class Day:
    def __init__(self, day: int):
        self.day = day
        root = Path(__file__).resolve().parent
        self.day_dir = root / f"day-{day}"
        self.input_path = self.day_dir / "input"
        self.data = self.read_input()

    def read_input(self):
        with open(self.input_path) as f:
            data = [line.strip() for line in f.readlines()]

        if len(data) == 1:
            return data[0]
        else:
            return data

    def run(self):
        print(f"--- Day {self.day:02} ---")

        start = time.perf_counter()
        silver = self.solve_silver()
        mid = time.perf_counter()

        gold = self.solve_gold()
        end = time.perf_counter()

        print(f"Silver: {silver}   ({(mid - start)*1000:.2f} ms)")
        print(f"Gold:   {gold}     ({(end - mid)*1000:.2f} ms)")
        print()

    # Methods to override
    def solve_silver(self):
        raise NotImplementedError

    def solve_gold(self):
        raise NotImplementedError
    
# Example
from base import Day

class Day0x(Day):
    def solve_silver(self):
        return None

    def solve_gold(self):
        return None
    
if __name__ == "__main__":
    Day0x(0).run()