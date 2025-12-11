import sys
from pathlib import Path
from collections import defaultdict

sys.path.append(str(Path(__file__).resolve().parent.parent))

from base import Day
from functools import cache

class Graph:
    # Helper class that stores a graph and contains depth first search
    def __init__(self, graph, end_node):
        self.graph = graph
        self.end_node = end_node
    
    @cache
    def DFS(self, node):        
        # If node is out exit
        if node == self.end_node:
            return 1

        output = 0
        for child in self.graph[node]:
            output += self.DFS(child)
            
        return output
    

class Day11(Day):
    def solve_silver(self):
        # Parse input
        graph = self.parse_input()
        
        # Init graph class
        graphh = Graph(graph, end_node="out")
        num_paths = graphh.DFS('you')

        return num_paths

    def solve_gold(self):
        # Parse input
        graph = self.parse_input()
        
        # Find number of ways to get from 'svr' to 'fft'
        graphh = Graph(graph, end_node="fft")
        num_svr_fft = graphh.DFS("svr")

        # Number of ways to get from 'fft' to 'dac'
        graphh = Graph(graph, end_node="dac")
        num_fft_dac = graphh.DFS("fft")
        
        # Number of ways to get from 'dac' to 'out'
        graphh = Graph(graph, end_node="out")
        num_dac_out = graphh.DFS("dac")

        return num_svr_fft * num_fft_dac * num_dac_out
    
    def parse_input(self):
        # Parse input and return graph and inverted version
        graph = defaultdict(list)
        
        for row in self.data:
            row = row.split(" ")
            key = row[0].strip(':')
            graph[key] = row[1:]
                   
        return graph
    

if __name__ == "__main__":
    Day11(11).run()

