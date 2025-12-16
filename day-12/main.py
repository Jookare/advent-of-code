import sys
from pathlib import Path
from collections import defaultdict

sys.path.append(str(Path(__file__).resolve().parent.parent))

from base import Day
from itertools import groupby
import numpy as np

class Day12(Day):
    def solve_silver(self):
        regions, objects = self.parse_input()

        total = 0
        for i, region in enumerate(regions):
            
            grid_size, object_counts = region
            num_grid_cells = grid_size[0]*grid_size[1]

            num_obj_cells = 0
            for id, count in enumerate(object_counts):
                num_obj_cells += objects[id].sum()*count

            if num_grid_cells >= num_obj_cells:
                total += 1

        return total

    def solve_gold(self):
        # Parse input
       
        return None
    
    def parse_input(self):
        # Group everything until empty line
        blocks = [list(group) for key, group in groupby(self.data, key=bool) if key]

        # Map symbols to 0-1
        ch_map = {'.': 0, '#': 1}

        # Build the objects as dicts and numpy arrays
        objects = {}
        for block in blocks[:-1]:
            object = []
            for row in block[1:]:
                object += [[ch_map[ch] for ch in row]]
            obj_id = int(block[0].strip(":"))
            objects[obj_id] = np.array(object)

        # Build the regions
        regions = []
        # object_counts = []
        for grid in blocks[-1]:
            grid = grid.split(" ")
            region = tuple(int(ch) for ch in grid[0].strip(":").split("x"))
            object_counts = [int(ch) for ch in grid[1:]]
            regions += [(region, object_counts)]
                   
        return regions, objects
    

if __name__ == "__main__":
    Day12(12).run()

