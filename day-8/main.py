import sys
from pathlib import Path
from collections import defaultdict

sys.path.append(str(Path(__file__).resolve().parent.parent))

from base import Day
from functools import reduce
import math 


class Day08(Day):
    def solve_silver(self):
        
        inputs = [[int(val) for val in row.split(",")] for row in self.data]
        
        
        dists = {}
        for i, val1 in enumerate(inputs):
            distances = []
            # print(val1)
            for j, val2 in enumerate(inputs):
                if  j < i:
                    distances += [((val1[0] - val2[0])**2 + (val1[1] - val2[1])**2 + (val1[2] - val2[2])**2)]
            dists[i] = distances

        nodes = []
        for i in range(1000):
            minim = [(0,0), math.inf]
            for key in dists.keys():
                
                row = dists[key]
                # print(row)
                for id, val in enumerate(row[:key]):
                    if val > 0 and val < minim[1]:
                        minim = [(key, id), val]
                        
            key, id = minim[0]
            nodes += [(key, id)]
            dists[key][id] = 0
            
        nodes
                    
        connects = []
        for a, b in nodes:
            # print(a,b)
            new_item = True
            if len(connects) == 0:
                connects += [[a,b]]
            else:
                for circ in connects:
                    # print(a,b ,circ)
                    if a in circ and b in circ:
                        new_item = False
                        continue
                    elif a in circ:
                        circ += [b]
                        new_item = False
                        # break
                    elif b in circ:
                        circ += [a]
                        new_item = False
                        # break
                
                # combine existing paths
                arrays = []
                for id, ccc in enumerate(connects):
                    if a in ccc and b in ccc:
                        arrays.append(id)
                    elif b in ccc:
                        arrays.append(id)
                    elif a in ccc:
                        arrays.append(id)
                
                print(arrays)
                if len(arrays) == 2:
                    connects[arrays[0]] = list(set(connects[arrays[0]] + connects[arrays[1]]))
                    connects.pop(arrays[1])
                
                # print(arrays)
                # print(connects)
                if new_item:
                    connects += [[a,b]]
                

        lengths = [len(arr) for arr in connects]
        largest_circs = reduce(lambda a,b: a*b, sorted(lengths, reverse=True)[:3])
        print(largest_circs)
        return largest_circs

    def mul(self, x, y):
        return x * y
    
    
    def solve_gold(self):
       
        return None
if __name__ == "__main__":
    Day08(8).run()
