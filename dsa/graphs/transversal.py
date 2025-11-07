from typing import Any, Dict, List


class Graph:
    def __init__(self, size):
        self.size = size
        self.node_data = ['']*size
        self.adj_matrix = [[0]* size for _ in range(size)]
    
    def add_edge(self, u:int, v:int) -> None:
        """assuming it is a non-weighted undirected graph"""
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][v] = 1
    
    def add_node_data(self, node_idx, data):
        if 0 <= node_idx < self.size:
            self.node_data[node_idx] = data
    
    def get_adjacents(self, node_idx:int) -> List[Any]:
        """Returns the adjacency list given a node index"""
        index_list = [i for i in range(self.size) if self.adj_matrix[node_idx][i] == 1 or self.adj_matrix[i][node_idx]== 1]
        node_list = [data for data in self.node_data if self.node_data.index(data) in index_list]
        return sorted(node_list)
    
    def add_all_nodes(self, nodes:List[Any]) -> None:
        self.node_data = nodes
        
    def graph_from_dict(self, dct: Dict[Any, Any]) -> None:
        """Creates a graph from a Python Dict. The keys are the graph nodes and the values are the adjacency lists
        """
        if len(dct) != self.size:
            raise ValueError('The number of items in the graph dict must be equal to the value of the propert `size`')
        node_values = list(dct.keys())
        self.node_data = node_values
        for node, adj_lst in dct.items():
            node_idx = node_values.index(node)
            for neighbour in adj_lst:
                neighbour_idx = node_values.index(neighbour)
                self.adj_matrix[node_idx][neighbour_idx] = 1
    
    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(" ".join(map(str, row)))
        print("\nVertex Data:")
        for vertex, data in enumerate(self.node_data):
            print(f"Vertex {vertex}: {data}")

    def dfs(self, start_node_data):
        """When you get to a node N, visit one of its neighbours (not all his neighbours), and then a neighbour of the
        visited neighbour. Continue the chain reaction until no more node on that path. Then come back to N and repeat
        the same thing on another neighbour, until no more neighbour of N remains. Meanwhile, the action at N is done
        recursive on every node down the line
        """

        def dfs_helper(v: int, visited: List[bool]) -> None:
            visited[v] = True
            print(self.node_data[v], end=" ")
            for i in range(self.size):
                if self.adj_matrix[v][i] == 1 and not visited[i]:
                    dfs_helper(i, visited)

        visited = [False] * self.size
        start_node = self.node_data.index(start_node_data)
        dfs_helper(start_node, visited)

    def bfs(self, start_node_data)->List[Any]:
        """When you get to a node, you visit all its neighbours before visiting a neighbour of any of its neighbours
        Better implemented with queues
        """
        queue = [self.node_data.index(start_node_data)]
        visited = [False]* self.size
        visited[queue[0]] = True
        trv = []
        while queue:
            current_node = queue.pop(0)
            trv.append(self.node_data[current_node])
            print(self.node_data[current_node], end=" ")
            
            for i in range(self.size):
                if self.adj_matrix[current_node][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True
        return trv

    def is_cyclic_undirected(self) -> bool:
        """Cyclic detection for undirected uweighted graph using DFS"""
        visited = [False] * self.size

        def helper(v: int, visited: List[bool], parent: int) -> bool:
            """A helper function for use with is_cyclic_undirected method"""
            visited[v] = True

            for i in range(self.size):
                if self.adj_matrix[v][1] == 1:  # that is, a neighbour of v
                    if not visited[i]:
                        if helper(i, visited, v):
                            return True
                    if parent != i:  # A neighbour that is not the immediate parent of v
                        return True
            return False
        
        for i in range(self.size):
            if not visited[i]:
                if helper(i, visited, -1):
                    return True
        return False

    def is_cyclic_directed(self) -> bool:
        visited = [False] * self.size
        rec_stack = [False] * self.size

        def helper(v: int, visited: List[bool], rec_stack: List[bool]) -> bool:
            visited[v] = True
            rec_stack[v] = True

            for i in range(self.size):
                if self.adj_matrix[v][i] == 1:
                    if not visited[i]:
                        if helper(i, visited, rec_stack):
                            return True
                    elif rec_stack[i]:
                        return True
            return False
        
        for i in range(self.size):
            if not visited[i]:
                if helper(i, visited, rec_stack):
                    return True
        return False


# graph1 is undirected but graph2 is directed
graph1 = {
    "A": ["C", "B"],
    "B": ["A", "D", "C", "E"],
    "C": ["A", "D", "B"],
    "D": ["C", "B"],
    "E": ["B"],
}

graph2 = {
    "A": ["C", "B"],
    "B": ["C", "E"],
    "C": ["D"],
    "D": ["A", "B"],
    "E": ["C"],
}


gf = Graph(size=5)
gf.graph_from_dict(graph1)
# gf.print_graph()
gf.dfs('C')
print()
print('\nYYYYYY', gf.bfs("D"))
print(gf.is_cyclic_undirected())

gf2 = Graph(size=5)
gf2.graph_from_dict(graph2)
print(gf2.is_cyclic_directed())