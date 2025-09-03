# Matrix (2D Grid)
from collections import defaultdict, deque
from typing import Dict, List, Set


class Matrix:
    """This class uses MATRIX representation to solve some questions on GRAPH
    
    Three ways of representating graphs:
    1. Matrix--used in this class
    2. Adjacency Matrix--Not too frequently used
    3. Adjacency List--Used in the next class below
    """

    # Count paths (backtracking)
    def unique_path_count(self, grid, r, c, visit):
        """_summary_

        Count the unique paths from top-left to bottom-right. A single path may only move along zeros and can't visit the same cell more than once
        """
        ROWS, COLS = len(grid), len(grid[0])
        if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit or grid[r][c] == 1:
            return 0
        if r == ROWS - 1 and c == COLS - 1:
            return 1

        visit.add((r, c))

        count = 0
        count += self.unique_path_count(grid, r + 1, c, visit)
        count += self.unique_path_count(grid, r - 1, c, visit)
        count += self.unique_path_count(grid, r, c + 1, visit)
        count += self.unique_path_count(grid, r, c - 1, visit)

        visit.remove((r, c))
        return count

    def shortest_path_length(self, grid):
        """_summary_

        Find the length of the shortest path from the top-left to the bottom-right

        The idea in this implementation is not to get all the paths and find the shortest. It is to keep going; for the first path get to the end, stop and return that path-count. That will surely be the shortest path.
        Does not use recursion or backtracking
        Space Complexity: O(m*n)
        Time Complexity: O(m*n)
        """
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        queue.append((0, 0))
        visited.add((0, 0))

        length = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length

                neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # Relative positions
                for dr, dc in neighbors:
                    if (
                        min(r + dr, c + dc) < 0
                        or r + dr == ROWS
                        or c + dc == COLS
                        or (r + dr, c + dc) in visited
                        or grid[r + dr][c + dc] == 1
                    ):
                        continue
                    queue.append((r + dr, c + dc))
                    visited.add((r + dr, c + dc))
            length += 1


class AdjacencyList:
    """This class uses ADJACENCY LIST representation to solve some questions on GRAPH 
    These are the same problems above
    """
    
    def generate_adjacency_list[T](self, edges: List[List[T]])->Dict[T, List[T]]:
        """This function takes directed edges and build an adjacency list from it"""
        adj_list = {}
        for src, dst in edges:
            if src not in adj_list:
                adj_list[src] = []
            if dst not in adj_list:
                adj_list[dst] = []
            adj_list[src].append(dst)
        
        return adj_list

    def generate_adjacency_list2[T](self, edges: List[List[T]]) -> Dict[T, List[T]]:
        """This function takes directed edges and build an adjacency list from it, using built in Python defaultdict~~"""
        adj_list = defaultdict(list)
        for src, dst in edges:
            adj_list[src].append(dst)
            if dst not in adj_list:
                adj_list[dst] = []

        return dict(adj_list)

    def count_unique_paths[T](self, node:T, target:T, adjList: Dict[T, List[T]], visit:Set[T])->int:
        if node in visit:
            return 0
        if node == target:
            return 1
        
        count = 0
        visit.add(node)
        for neighbor in adjList[node]:
            count += self.count_unique_paths(neighbor, target, adjList, visit)
        visit.remove(node)

        return count
    
    def shortest_path[T](self, node: T, target: T, adjList: Dict[T, List[T]])->int:
        length = 0
        queue = deque()
        visit = set()
        visit.add(node)
        queue.append(node)

        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr == target:
                    return length

                for neighbor in adjList[curr]:
                    if neighbor not in visit:
                        visit.add(neighbor)
                        queue.append(neighbor)
            length += 1
        return length
    
EDGES = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]
grid = [
    [0, 0, 0, 0], 
    [1, 1, 0, 0], 
    [0, 0, 0, 1], 
    [0, 1, 0, 0]
    ]
GRID_EDGES = [["B", "A"], ["B", "B"], ["C", "D"], ["D", "B"]]
ADJ_LIST_EDGES = {
    "A": [],
    "B": ["A", "B"],
    "C": ["D"],
    "D": ["B"]
}


mtrx = Matrix()
print(">>>>>>>>>Shortest path", mtrx.shortest_path_length(grid))
print(">>>>>>>>>Number of unique paths", mtrx.unique_path_count(grid, 0, 0, set()))
print("YYYYY", AdjacencyList().generate_adjacency_list(GRID_EDGES))
print("YYYYY2", AdjacencyList().generate_adjacency_list2(GRID_EDGES))