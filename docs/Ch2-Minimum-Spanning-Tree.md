# Chapter 2. Graph Theory

## Minimum Spanning Tree

**What is a Spanning Tree?**

Given an undirected and connected graph $G=(V,E)$ (This notation is graph representation in Discrete Mathematics: means graph **G** has a set of **V**ertices and a set of **E**dges), a spanning tree of the graph G is a tree that spans G (that is, it includes every vertex of G) and is a subgraph of G (every edge in the tree belongs to G)

![](https://static.packt-cdn.com/products/9781788833738/graphics/4039b410-53fe-4887-923b-3a3ba938e32d.png)

**What is a Minimum Spanning Tree?**

The cost of the spanning tree is the sum of the **weights** of all the **edges** in the tree. There can be many spanning trees. Minimum spanning tree is the spanning tree where the cost is minimum among all the spanning trees. There also can be many minimum spanning trees.

![](https://he-s3.s3.amazonaws.com/media/uploads/146b47a.jpg)

Minimum spanning tree has direct application in the design of networks. It is used in algorithms approximating the travelling salesman problem, multi-terminal minimum cut problem and minimum-cost weighted perfect matching. Other practical applications are:

1. Cluster Analysis
2. Handwriting recognition
3. Image segmentation

### Prim's Algorithms

Prim’s Algorithm use Greedy approach to find the minimum spanning tree. We start from one vertex and keep adding edges with the lowest weight until we reach our goal.

**The steps for implementing Prim's algorithm:**

1. Initialize the minimum spanning tree with a vertex chosen at random.
2. Find all the edges that connect the tree to new vertices, find the minimum and add it to the tree
3. Keep repeating step 2 until we get a minimum spanning tree

![](https://i.stack.imgur.com/TTwpR.png)

**Code**: [[src code]](./codes/algorithms/prims.py)

```python
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
```
