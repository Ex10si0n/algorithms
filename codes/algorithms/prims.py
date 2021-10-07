class Graph:

    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges

    def adjacency_list(self):
        G = {}
        for i in range(len(self.edges)):
            from_node, to_node, val = self.edges[i].split(' ')
            if from_node in G.keys(): G[from_node].append((to_node, val))
            else: G[from_node] = [(to_node, val)]
            if to_node in G.keys(): G[to_node].append((from_node, val))
            else: G[to_node] = [(from_node, val)]
        return G


class Prims:

    def __init__(self, graph):
        self.visited = []
        self.mst = []
        self.graph = graph
        self.N = len(self.graph.keys())
        self.visited.append(list(graph.keys())[0])

    def prims(self):
        while len(self.mst) < self.N - 1:
            _min = float('inf')
            from_node = to_node = None;
            for node in self.visited:
                for _next in self.graph[node]:
                    next_node = _next[0]
                    edge_val = int(_next[1])
                    if next_node not in self.visited:
                        if _min > edge_val:
                            _min = edge_val
                            from_node = node
                            to_node = next_node

            e = (from_node, to_node, _min)
            self.visited.append(to_node)
            self.mst.append(e)
        return self.mst


if __name__ == "__main__":
    vertices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    edges = ['a b 4', 'b c 8', 'c d 7', 'd e 9', 'e f 10', 'f g 2', 'g h 1',\
             'h i 7', 'a h 8', 'g i 6', 'c i 2', 'c f 4', 'd f 14', 'b h 11']
    graph = Graph(vertices, edges).adjacency_list()
    mst = Prims(graph).prims()
    print(mst)

