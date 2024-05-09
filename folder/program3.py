from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def prim_mst(self):
        visited = set()
        mst = []

        start_vertex = next(iter(self.graph))  # Choose arbitrary starting vertex
        visited.add(start_vertex)

        while len(visited) < len(self.graph):
            min_edge = None
            min_weight = float('inf')

            for u in visited:
                for v, weight in self.graph[u]:
                    if v not in visited and weight < min_weight:
                        min_edge = (u, v)
                        min_weight = weight

            if min_edge:
                u, v = min_edge
                visited.add(v)
                mst.append((u, v, min_weight))

        return mst

# Example usage
g = Graph()
g.add_edge('A', 'B', 2)
g.add_edge('A', 'C', 3)
g.add_edge('B', 'C', 1)
g.add_edge('B', 'D', 1)
g.add_edge('C', 'D', 2)

mst = g.prim_mst()
print("Edges in the Minimum Spanning Tree:")
for edge in mst:
    print(edge)
