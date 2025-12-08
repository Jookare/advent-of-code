import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from base import Day
from operator import add

class Day04(Day):
    def solve_silver(self):
        
        # index_array = self.create_index_array(self.data)
    
        # counter = 0
        # for row_id in range(1,len(index_array)-1):
        #     for col_id in range(1,len(index_array[0])-1):
        #         sum_3x3 = self.get_3x3_sum(index_array, row_id, col_id)
        #         if sum_3x3 < 5:
        #             counter +=1
                    
        # return (counter)
        index_array = self.create_index_array(self.data)
        sum_array = self.pad_index_array(index_array)

        counter = 0
        for row_id in range(1,len(sum_array)-1):
            for col_id in range(1,len(sum_array[0])-1):
                # 3 by 3 sum so also the paper roll itself is computer
                if index_array[row_id-1][col_id-1] == 1 and sum_array[row_id][col_id] < 4:
                    counter +=1
                    
        return (counter)

    def solve_gold(self):
        index_array = self.create_index_array(self.data)

        paper_removed = 0
        counter = 10
        while counter > 0:
            counter = 0
            sum_array = self.pad_index_array(index_array)
            for row_id in range(1,len(sum_array)-1):
                for col_id in range(1,len(sum_array[0])-1):
                    if index_array[row_id-1][col_id-1] == 1 and sum_array[row_id][col_id] < 4:
                        counter +=1
                        index_array[row_id-1][col_id-1] = 0
            paper_removed += counter
        return (paper_removed)
    
        # index_array = self.create_index_array(self.data)

        # paper_removed = 0
        # counter = 10
        # while counter > 0:
        #     counter = 0
        #     for row_id in range(1,len(index_array)-1):
        #         for col_id in range(1,len(index_array[0])-1):
        #             sum_3x3 = self.get_3x3_sum(index_array, row_id, col_id)
        #             if sum_3x3 < 5:
        #                 counter +=1
        #                 index_array[row_id][col_id] = 0
        #     paper_removed += counter
        # return paper_removed

    def create_index_array(inputs):
        "Improved grid building, where 0 is free spot and 1 is paper"
        
        inner_array = [
            [int(ch == '@') for ch in row] 
            for row in inputs
        ]
        
        # No need for insert as one can use sum
        padded_rows = [
            [0] + row + [0]
            for row in inner_array
        ]
            
        width = len(padded_rows[0])
        pad = [[0]*width]
        
        return pad + padded_rows + pad
    
    def get_3x3_sum(self, grid, r, c):
        if grid[r][c] == 0:
            return 9
        return sum([sum(row[c-1:c+2]) for row in grid[r-1:r+2]])

if __name__ == "__main__":
    Day04(4).run()