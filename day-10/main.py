import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from base import Day
import numpy as np
from itertools import combinations
from scipy.optimize import linprog

class Day10(Day):
    def solve_silver(self):
        
        all_diagrams, all_buttons, all_joltages = self.parse_inputs()
        
        num_cases = len(all_diagrams)

        total_presses = 0
        for i in range(num_cases):
            print(i)
            
            diagram = np.array(all_diagrams[i])
            buttons = all_buttons[i]

            flag = False
            num_presses = 1000
            for j in range(len(buttons)):
                comb = list(combinations(buttons, j))
                for c in comb:
                    test_case = np.zeros_like(diagram)
                    for press in c:
                        for val in press:
                            test_case[val] = (test_case[val] + 1) % 2
                    if np.all(test_case == diagram):
                        flag = True
                        num_presses = len(c)
                        break
                if flag:
                    break
            if num_presses < 1000:
                total_presses += num_presses
            else:
                print("problem")
        return total_presses
                
    def solve_gold(self):

        all_diagrams, all_buttons, all_joltages = self.parse_inputs()
        
        num_presses = 0
        # Turn buttons into Matrix
        for id, buttons in enumerate(all_buttons):
            
            b = np.array(all_joltages[id])
            
            # Num values and variables
            N_val = len(all_joltages[id])
            N_var = len(buttons)
            A = np.zeros((N_val, N_var))
            
            for i, button in enumerate(buttons):
                A[button, i] = 1
            
            c = np.ones(A.shape[1])
            integrality = np.ones(A.shape[1])
            bounds = [(0, int(max(b))) for i in range(A.shape[1])]
            
            result = linprog(c, A_eq=A, b_eq=b, bounds=bounds, integrality=integrality)
            print(result.fun, result.status)
            num_presses += int(result.fun)
        return num_presses
    
    
    def parse_inputs(self):
        map = {'.': 0, '#': 1}

        all_diagrams = []
        all_buttons = []
        all_joltages = []

        for row in self.data:
            tokens = row.split(" ")
            diagram_token = None
            button_tokens = []
            joltage_token = None
            for t in tokens:
                if t.startswith('['):
                    diagram_token = t
                elif t.startswith('('):
                    button_tokens.append(t)
                elif t.startswith('{'):
                    joltage_token = t


            diagram_str = diagram_token.strip('[]')
            diagram = [map[ch] for ch in diagram_str]

            temp_buttons = []
            for t in button_tokens:
                inner = t.strip('()')
                nums = [int(x) for x in inner.split(',')]
                temp_buttons.append(nums)


            joltage_str = joltage_token.strip('{}')
            joltage = [int(x) for x in joltage_str.split(',')]
            
            all_diagrams.append(diagram)
            all_buttons.append(temp_buttons)
            all_joltages.append(joltage)
            
        return all_diagrams, all_buttons, all_joltages
    
if __name__ == "__main__":
    Day10(10).run()
