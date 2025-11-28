# Matrix (2D Grid)
from collections import defaultdict, deque
from typing import Dict, List, Optional, Set


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Matrix:
    """This class uses MATRIX representation to solve some questions on GRAPH
    
    Three ways of representating graphs:
    1. Matrix--used in this class
    2. Adjacency Matrix--Not too frequently used
    3. Adjacency List--Used in the next class below
    """

    # Count paths (backtracking, dfs)
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

        visit.remove((r, c))  # Mark as unvisited so it can serve as part of another possible route
        return count

    def shortest_path_length(self, grid):
        """_summary_

        Find the length of the shortest path from the top-left to the bottom-right

        The idea in this implementation is not to get all the paths and find the shortest. It is to keep going; for the first path get to the end, stop and return that path-count. That will surely be the shortest path.
        Does not use recursion or backtracking. Uses BFS

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
                    nr = r + dr
                    nc = c + dc
                    if min(nr, nc) < 0 or nr == ROWS or nc == COLS or (nr, nc) in visited or grid[nr][nc] == 1:
                        continue
                    queue.append((nr, nc))
                    visited.add((nr, nc))
            length += 1

    def num_islands(self, grid: List[List[str]]) -> int:
        """_Neetcode_Medium_

        Given a 2D grid `grid` where '1' represents land and '0' represents water, count and return the number of islands.
        An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. You may assume water is surrounding the grid (i.e., all the edges are water).

        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        """
        rows, cols = len(grid), len(grid[0])

        def dfs(i, j):
            """Depth-first traversal to mark members of the island as zero, so we do not inadvertently count it again. An alternative to marking them as zero would be to add them in a hash set"""
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            dfs(i, j + 1)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i - 1, j)

        island_count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    island_count += 1
                    dfs(i, j)
        return island_count

    def max_area_of_island(self, grid: List[List[int]]) -> int:
        """_Neetcode_Medium_

        You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).
        An island is defined as a group of 1's connected horizontally or vertically. You may assume all four edges of the grid are surrounded by water.
        The area of an island is defined as the number of cells within the island.
        Return the maximum area of an island in grid. If no island exists, return 0.
        """
        rows, cols = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0:
                return 0
            area = 1
            grid[i][j] = 0
            area += dfs(i, j + 1)
            area += dfs(i, j - 1)
            area += dfs(i + 1, j)
            area += dfs(i - 1, j)
            return area

        max_island = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_island = max(max_island, dfs(i, j))
        return max_island

    def oranges_rotting(self, grid: list[list[int]]) -> int:
        """_Neetcode_Medium

        You are given a 2-D matrix grid. Each cell can have one of three possible values:

        0 representing an empty cell
        1 representing a fresh fruit
        2 representing a rotten fruit
        Every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, then the fresh fruit also becomes rotten.

        Return the minimum number of minutes that must elapse until there are zero fresh fruits remaining. If this state is impossible within the grid, return -1.
        """
        _, FRESH, ROTTEN = 0, 1, 2
        m, n = len(grid), len(grid[0])
        num_fresh = 0
        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == ROTTEN:
                    queue.append((i, j))
                elif grid[i][j] == FRESH:
                    num_fresh += 1
        if num_fresh == 0:
            return 0

        num_minutes = -1
        while queue:
            q_size = len(queue)
            num_minutes += 1
            for _ in range(q_size):
                i, j = queue.popleft()
                for r, c in [(i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j)]:
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == FRESH:
                        grid[r][c] = ROTTEN
                        num_fresh -= 1
                        queue.append((r, c))

        if num_fresh > 0:
            return -1
        return num_minutes


class AdjacencyList:
    """This class uses ADJACENCY LIST representation to solve some questions on GRAPH
    These are the same problems solved using MATRIX above
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
        """Uses DFS"""
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


def cloneGraph(node: Optional[Node]) -> Optional[Node]:
    """_Neetcode_Medium_
    Given a node in a connected undirected graph, return a `deep copy` of the graph.
    Each node in the graph contains an integer value and a list of its neighbors.
    The graph is shown in the test cases as an adjacency list. An adjacency list is a mapping of nodes to lists, used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.
    For simplicity, nodes values are numbered from `1` to `n`, where `n` is the total number of nodes in the graph. The index of each node within the adjacency list is the same as the node's value (1-indexed). For example, [[2],[1,3],[2]] will translate to: {1: [2], 2: [1,3], 3:[2]}
    The input node will always be the first node in the graph and have `1` as the value.

    Time Complexity: O(V+E)
    Space Complexity: O(V)
    """
    if not node:
        return None

    oldToNew = {}
    oldToNew[node] = Node(node.val)
    q = deque([node])

    while q:
        cur = q.popleft()
        for nei in cur.neighbors:
            if nei not in oldToNew:
                oldToNew[nei] = Node(nei.val)
                q.append(nei)
            oldToNew[cur].neighbors.append(oldToNew[nei])

    return oldToNew[node]


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """Neetcode_Medium_

    You are given an array `prerequisites` where `prerequisites[i]` = `[a, b]` indicates that you must take course `b` first if you want to take course `a`.
    The pair [0, 1], indicates that you must take course 1 before taking course 0.
    There are a total of `numCourses` courses you are required to take, labeled from 0 to `numCourses - 1`.
    Return true if it is possible to finish all courses, otherwise return false.

    The solution for this problem is to check for CYCLIC GRAPH. If a cycle is detected, we return false
    a la Greg Hogg
    """
    # Generate Adjacency List dict
    pre_map = {i: [] for i in range(numCourses)}
    for crs, pre in prerequisites:
        pre_map[crs].append(pre)

    UNVISITED, VISITING, VISITED = 0, 1, 2
    states = [UNVISITED] * numCourses  # List holding the initial states of all the nodes

    def dfs(node):
        state = states[node]
        if state == VISITED:
            return True
        elif state == VISITING:  # CYCLE detected
            return False

        states[node] = VISITING
        for nei in pre_map[node]:
            if not dfs(nei):
                return False

        states[node] = VISITED
        return True

    for c in range(numCourses):
        if not dfs(c):
            return False
    return True


def island_perimeter(grid: list[list[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    perimeter = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                perimeter += 4
                for diff in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    r = i + diff[0]
                    c = j + diff[1]
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                        perimeter -= 1
    return perimeter


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