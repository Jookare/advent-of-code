import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from base import Day
import numpy as np
from collections import defaultdict

class Day09(Day):
    def solve_silver(self):
        dists = []
        inputs = [[int(val) for val in row.split(",")] for row in self.data]
        
        # Compute distances between all nodes
        for i, val1 in enumerate(inputs):
            for j, val2 in enumerate(inputs):
                if j < i:
                    dists += [(abs(val1[0] - val2[0])+1) * (abs(val1[1] - val2[1])+1)]
                    
        return max(dists)
                
    def solve_gold(self):
        inputs = [[int(val) for val in row.split(",")] for row in self.data]
        inputs = np.array(inputs, dtype=np.int64)
        N_inputs = len(inputs)

        # Check if we need to turn points around.  
        # Current solution works only for clockwise traversal 
        min_x_id = np.argmin(inputs[:,0])
        cur_point = inputs[min_x_id]
        next_point = inputs[min_x_id+1]

        print(cur_point, next_point)
        if cur_point[1] > next_point[1]:
            inputs = inputs[::-1]

        # Create helper version of the inputs
        looped_inputs = np.r_[inputs, inputs]
        horizontal_edges, vertical_edges = self.compute_edges(looped_inputs, N_inputs)
       
        # pre-sort keys 
        vertical_keys = sorted(vertical_edges.keys())
        horizontal_keys = sorted(horizontal_edges.keys())
                
        print("\nloop starts:")
        max_area = 0
        for i in range(N_inputs-1):
            prev_point = looped_inputs[i - 1]
            mid_point = looped_inputs[i]
            next_point = looped_inputs[i + 1]
            v1 = prev_point - mid_point
            v2 = next_point - mid_point
            cross_prod = self.cross2d(v1, v2)

            # Compute vector from midpoint to all points
            vecs = inputs - mid_point
            dots1 = vecs @ v1
            dots2 = vecs @ v2
            
            # Mask for valid points
            if cross_prod < 0:
                mask = (dots1 <= 0) | (dots2 <= 0)
            else:
                mask = (dots1 >= 0) & (dots2 >= 0)

            # Exclude the point itself
            mid_point_mask = ~np.all(vecs == 0, axis=1)
            mask &= mid_point_mask
            valid_points = inputs[mask]
            
            for corner in valid_points:
                # Points are in line so just compute area 
                min_x = min(corner[0], mid_point[0])
                max_x = max(corner[0], mid_point[0])
                min_y = min(corner[1], mid_point[1])
                max_y = max(corner[1], mid_point[1])

                # Select keys that are between the x and y values
                relevant_x_keys = [x for x in vertical_keys if min_x < x < max_x]
                relevant_y_keys = [y for y in horizontal_keys if min_y < y < max_y]
                
                blocked = False
                # Go through vertical edges
                for x in relevant_x_keys:
                    for edge in vertical_edges.get(x, []):
                        if edge[1] <= min_y or edge[0] >= max_y:
                            continue
                        else:
                            blocked = True
                            break
                    if blocked: 
                        break
                    
                for y in relevant_y_keys:
                    for edge in horizontal_edges.get(y, []):
                        if edge[1] <= min_x or edge[0] >= max_x:
                            continue
                        else:
                            blocked = True
                            break
                    if blocked: 
                        break

                if not blocked:
                    area = (max_x - min_x + 1) * (max_y - min_y + 1)
                    max_area = max(max_area, area)
        
        return max_area
    
    def cross2d(self, v1,v2):
        return v1[0]*v2[1] - v1[1]*v2[0]

    def compute_edges(self, looped_inputs, N_inputs):
        # Pre-compute edges
        vertical_edges = defaultdict(list)
        horizontal_edges = defaultdict(list)
        for i in range(N_inputs):
            p1 = looped_inputs[i]
            p2 = looped_inputs[i+1]
            start = np.minimum(p1, p2)
            end   = np.maximum(p1, p2)
            
            if start[0] == end[0]: # vertical
                vertical_edges[start[0]].append((start[1], end[1]))
            elif start[1] == end[1]: # horizontal
                horizontal_edges[start[1]].append((start[0], end[0]))
        return horizontal_edges, vertical_edges

if __name__ == "__main__":
    Day09(9).run()
