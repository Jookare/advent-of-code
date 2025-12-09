import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from base import Day
import numpy as np


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
        inputs = np.array(inputs)
        
        min_x_id = np.argmin(inputs[:,0])
        cur_point = inputs[min_x_id]
        next_point = inputs[min_x_id+1]

        print(cur_point, next_point)
        if cur_point[1] > next_point[1]:
            inputs = inputs[::-1]
            
        looped_inputs = np.r_[inputs, inputs]
        
        print("\nloop starts:")
        N_inputs = len(inputs)

        max_area = 0
        for i in range(N_inputs):
            prev_point = looped_inputs[i - 1]
            mid_point = looped_inputs[i]
            next_point = looped_inputs[i + 1]
            v1 = mid_point - prev_point
            v2 = mid_point - next_point
            cross_prod = self.cross2d(v1, v2)

            
            valid_points = []
            # NOTE: There is currently issue in here that the convex and concave is not being computed correctly
            for j, coord in enumerate(inputs):
                if not np.array_equal(coord, mid_point):
                    
                    vec =  coord - mid_point 
                    dot1 = np.dot(v1, vec)
                    dot2 = np.dot(v2, vec)
                    
                    # angle is convex and point is within the region
                    if cross_prod < 0 and dot1 >= 0 and dot2 >= 0:
                        valid_points += [coord]
                        
                    # angle is concave and point is within the region
                    elif cross_prod > 0 and dot1 <= 0 and dot2 <= 0:
                        valid_points += [coord]
                        
                    else:
                        continue
        
            # For all valid points loop
            for corner in valid_points:
                area = (abs(mid_point[0] - corner[0]) + 1) * (abs(mid_point[1] - corner[1]) + 1)
                for coord in valid_points:
                    min_x = min(corner[0], mid_point[0])
                    max_x = max(corner[0], mid_point[0])
                    min_y = min(corner[1], mid_point[1])
                    max_y = max(corner[1], mid_point[1])
                    
                    # Check if there is vertical line within the rectangle
                    if (coord[0] > min_x and coord[0] < max_x):
                        pos = np.where((inputs == coord).all(axis=1))[0]
                        prev = looped_inputs[pos-1][0]
                        next = looped_inputs[pos+1][0]
                        if prev[0] == coord[0]:
                            bound = prev
                        else:
                            bound = next 
                        
                        line_max_y = max(bound[1], coord[1])
                        line_min_y = min(bound[1], coord[1])
                        
                        # Check if the line is outside of the current rectangle
                        if line_max_y <= min_y or line_min_y >= max_y:
                            continue
                        else:
                            area = 0
                            break
                        
                    # Check if there is horizontal line within the rectangle
                    elif (coord[1] > min_y and coord[1] < max_y):
                        pos = np.where((inputs == coord).all(axis=1))[0]
                        prev = looped_inputs[pos-1][0]
                        next = looped_inputs[pos+1][0]
                        if prev[1] == coord[1]:
                            bound = prev
                        else:
                            bound = next 
                        line_max_x = max(bound[0], coord[0])
                        line_min_x = min(bound[0], coord[0])
                        
                        # Check if the line is outside of the current rectangle
                        if line_max_x <= min_x or line_min_x >= max_x:
                            continue
                        else:
                            area = 0
                            break
                    
                if area > max_area:
                    max_area = area
    
        return max_area
    
    def cross2d(self, v1,v2):
        return v1[0]*v2[1] - v1[1]*v2[0]

if __name__ == "__main__":
    Day09(9).run()
