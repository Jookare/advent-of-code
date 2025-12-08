import sys
from pathlib import Path
from collections import defaultdict

sys.path.append(str(Path(__file__).resolve().parent.parent))

from base import Day
from functools import reduce


class Day08(Day):
    def solve_silver(self):
        inputs = [[int(val) for val in row.split(",")] for row in self.data]
        N_inputs = len(inputs)
        
        # Number of closest nodes
        N = 1000
        
        # Compute distances between all nodes
        dists = self.compute_dist(inputs)
        _, _, connects = self.find_nodes(dists[:N], N_inputs)
        lengths = [len(arr) for arr in connects]
        largest_circs = reduce(lambda a,b: a*b, sorted(lengths, reverse=True)[:3])
        
        return largest_circs
                
    def solve_gold(self):
        inputs = [[int(val) for val in row.split(",")] for row in self.data]
        N_inputs = len(inputs)
        
        # Compute distances between all nodes
        dists = self.compute_dist(inputs)

        a, b, _ = self.find_nodes(dists, N_inputs)

        return inputs[a][0]*inputs[b][0]
    
    def compute_dist(self, inputs):
        """Computes distances between all pairs of points"""
        dists = []
        for i, val1 in enumerate(inputs):
            for j, val2 in enumerate(inputs):
                if j < i:
                    dists += [(i,j, ((val1[0] - val2[0])**2 + (val1[1] - val2[1])**2 + (val1[2] - val2[2])**2))]
        
        dists = sorted(dists, key=lambda x: x[2])
        return dists
    
    def find_nodes(self, dists, N_inputs):
        connects = []
        for a, b, D in dists:
            new_item = True
            if len(connects) == 0:
                connects += [[a,b]]
            else:
                # Find if a or b already in some circuit
                for circ in connects:
                    if a in circ and b in circ:
                        new_item = False
                        continue
                    elif a in circ:
                        circ += [b]
                        new_item = False
                        break
                    elif b in circ:
                        circ += [a]
                        new_item = False
                        break
                
                arrays = []
                # Find in which array a and b exists
                for id, circ in enumerate(connects):
                    if a in circ and b in circ:
                        arrays.append(id)
                    elif b in circ:
                        arrays.append(id)
                    elif a in circ:
                        arrays.append(id)
                
                # If a and b are in two different arrays, combine those
                if len(arrays) == 2:
                    connects[arrays[0]] = list(set(connects[arrays[0]] + connects[arrays[1]]))
                    connects.pop(arrays[1])
                    
                # If all values in connects, stop iteration
                if len(connects[0]) == N_inputs:
                    # print(connects, a, b)
                    break
                
                # If a and b not in any array make new one
                if new_item:
                    connects += [[a,b]]
                
        return (a,b, connects)

if __name__ == "__main__":
    Day08(8).run()
