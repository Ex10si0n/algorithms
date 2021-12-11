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

## Depth First Search

Depth First Search (abbr. DFS) (深度优先搜索) is an algorithm for graph or tree traversal or searching a specific node in a tree. It adopts [recursion](https://github.com/Ex10si0n/Algorithms#recursion), so you should understand recursion for a better learning of DFS. For a simple example, there is code snippet of DFS.

Consider the maze is the following:

```
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.
#. .#. . . . . . . .#. . . . . . . .#. .#.
#. .#. .#.#.#.#.#. .#.#.#. .#.#.#. .#. .#.
#. . . .#. . . .#. .#. . . .#. .#. . . .#.
#.#.#.#.#.#.#. .#. .#. .#.#.#. .#.#.#. .#.
#. . . . . . . .#. .#. . . .#. . . . . .#.
#. .#.#.#.#.#.#.#. .#. .#. .#.#.#. .#.#.#.
#. . . . . . . . . .#. .#. . . .#. . . .#.
#. .#.#.#.#.#.#.#.#.#.#.#.#.#. .#.#.#. .#.
#. .#. . . . . . . .#. . . . . .#. .#. .#.
#. .#.#.#. .#.#.#. .#. .#.#.#.#.#. .#. .#.
#. . . .#. . . .#. . . .#. . . .#. .#. .#.
#.#.#. .#.#.#. .#.#.#.#.#. .#. .#. .#. .#.
#. .#. . . . . .#. . . . . .#. .#. .#. .#.
#. .#.#.#.#.#.#.#.#.#.#.#. .#. .#. .#. .#.
#. . . . . .#. . . . . .#. .#. . . .#. .#.
#. .#.#.#.#.#. .#. .#. .#. .#. .#.#.#. .#.
#. . . . . .#. .#. .#. . . .#. .#. . . .#.
#. .#.#.#. .#. .#. .#.#.#.#.#.#.#. .#.#.#.
#. . . .#. . . .#. . . . . . . . . . . .#.
#.#.#.#.X.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.
```

To let computer program walk through the maze, we can adopt DFS in the problem solving program. Here is the pseudo code.

```python
def dfs(now_position):
    visited.append(now_position)
    if now_position == exit_position:
    	return True
    # Try to step on adjacent position
    for dir in "←↓↑→":
        next_position = now_position.step(dir)
        # The case when next position can be stepped on
        if not next_position is "#" and next_position not in visited:
            dfs(next_position)
```

Please try to solve the previous maze problem by referencing pseudo code (Or any type of Algorithms you like or you have created). And mark the path using `*`.

Here is the code to help your program reading and storing the maze. [[src code]](./codes/algorithms/maze_parser.py)

```python
maze = '''#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.
          #.#.#. . . . . . . .#. . . . . . . .#. .#.
          #. .#. .#.#.#.#.#. .#.#.#. .#.#.#. .#. .#.
          #. . . .#. . . .#. .#. . . .#. .#. . . .#.
          #.#.#.#.#.#.#. .#. .#. .#.#.#. .#.#.#. .#.
          #. . . . . . . .#. .#. . . .#. . . . . .#.
          #. .#.#.#.#.#.#.#. .#. .#. .#.#.#. .#.#.#.
          #. . . . . . . . . .#. .#. . . .#. . . .#.
          #. .#.#.#.#.#.#.#.#.#.#.#.#.#. .#.#.#. .#.
          #. .#. . . . . . . .#. . . . . .#. .#. .#.
          #. .#.#.#. .#.#.#. .#. .#.#.#.#.#. .#. .#.
          #. . . .#. . . .#. . . .#. . . .#. .#. .#.
          #.#.#. .#.#.#. .#.#.#.#.#. .#. .#. .#. .#.
          #. .#. . . . . .#. . . . . .#. .#. .#. .#.
          #. .#.#.#.#.#.#.#.#.#.#.#. .#. .#. .#. .#.
          #. . . . . .#. . . . . .#. .#. . . .#. .#.
          #. .#.#.#.#.#. .#. .#. .#. .#. .#.#.#. .#.
          #. . . . . .#. .#. .#. . . .#. .#. . . .#.
          #. .#.#.#. .#. .#. .#.#.#.#.#.#.#. .#.#.#.
          #. . . .#. . . .#. . . . . . . . . . .#.#.
          #.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.'''

def maze_parser(maze):
    res = []
    for line in maze.strip().split('\n'):
        line = line.strip().split('.')
        res.append(line)
    return res

if __name__ == '__main__':
    maze = maze_parser(maze)
    start = [1, 1]
    end = [19, 19]
```

Using the above parser, the maze can be processed into an 2-D matrix (or array). you can access any `(x, y)` by invoking `maze[x][y]`.

Please try to understand the psedo code first. Solution changes several codes due to specific problem solving. `path` list is recorded in each `dfs()` function's parameter list.

> Why the `path` list should be recorded in the `dfs()` parameter list but not as instance variable?

**Sol.** [[src code]](./codes/algorithms/dfs_maze.py)

```python
maze = '''#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.
          #.#.#. . . . . . . .#. . . . . . . .#. .#.
          #. .#. .#.#.#.#.#. .#.#.#. .#.#.#. .#. .#.
          #. . . .#. . . .#. .#. . . .#. .#. . . .#.
          #.#.#.#.#.#.#. .#. .#. .#.#.#. .#.#.#. .#.
          #. . . . . . . .#. .#. . . .#. . . . . .#.
          #. .#.#.#.#.#.#.#. .#. .#. .#.#.#. .#.#.#.
          #. . . . . . . . . .#. .#. . . .#. . . .#.
          #. .#.#.#.#.#.#.#.#.#.#.#.#.#. .#.#.#. .#.
          #. .#. . . . . . . .#. . . . . .#. .#. .#.
          #. .#.#.#. .#.#.#. .#. .#.#.#.#.#. .#. .#.
          #. . . .#. . . .#. . . .#. . . .#. .#. .#.
          #.#.#. .#.#.#. .#.#.#.#.#. .#. .#. .#. .#.
          #. .#. . . . . .#. . . . . .#. .#. .#. .#.
          #. .#.#.#.#.#.#.#.#.#.#.#. .#. .#. .#. .#.
          #. . . . . .#. . . . . .#. .#. . . .#. .#.
          #. .#.#.#.#.#. .#. .#. .#. .#. .#.#.#. .#.
          #. . . . . .#. .#. .#. . . .#. .#. . . .#.
          #. .#.#.#. .#. .#. .#.#.#.#.#.#.#. .#.#.#.
          #. . . .#. . . .#. . . . . . . . . . .#.#.
          #.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.'''

def maze_parser(maze):
    res = []
    for line in maze.strip().split('\n'):
        line = line.strip().split('.')
        res.append(line)
    return res

class Search:
    def __init__(self, maze, start, end):
        self.visited = []
        self.maze = maze
        self.start = start
        self.end = end
        self.size = end[0] + 2
        self.move_dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        self.path = None
        self.solve()

    def move(self, _from, towards):
        return [_from[0]+towards[0], _from[1]+towards[1]]

    def draw_path(self):
        for step in self.path:
            self.maze[step[0]][step[1]] = '*'

    def print_maze(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.maze[i][j], end=' ')
            print()

    def solve(self):
        self.dfs(self.start, path=[])
        self.path = [self.path[i:i+2] for i in range(0, len(self.path), 2)]
        self.draw_path()
        self.print_maze()

    def dfs(self, now_position, path):
        self.visited.append(now_position)
        if now_position == self.end:
            self.path = path
            return True
        for _dir in self.move_dir:
            next_position = self.move(_from=now_position, towards=_dir)
            x = next_position[0]; y = next_position[1]
            if next_position not in self.visited and maze[x][y] != '#':
                self.dfs(next_position, path+now_position)
        return False


if __name__ == '__main__':
    maze = maze_parser(maze)
    start = [1, 1]
    end = [19, 19]
    search = Search(maze, start, end)
```

### LC200 Number of Islands

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return *the number of islands*.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 **Example 1:**

```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

**Example 2:**

```
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

**Constraints:**

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 300`
- `grid[i][j]` is `'0'` or `'1'`.

#### Sol.

```python
class Solution:
    
    def dfs(self, grid, x, y):
        move_dir = [[-1, 0], [0, 1], [0, -1], [1, 0]]
        grid[x][y] = '0'
        for _dir in move_dir:
            next_x = x + _dir[0]
            next_y = y + _dir[1]
            if next_x >= 0 and next_y >= 0 and next_x < len(grid) and next_y < len(grid[0]):
                if grid[next_x][next_y] == '1':
                    self.dfs(grid, next_x, next_y)
        
    
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    self.dfs(grid, x, y)
                    res += 1
        return res
```

## Shortest Path I

Here is the map of Ex10si0n island. He designed the arrangement of each town (namely A B C D E F G -town) with roads. When the tourist go through a certain path, he or she will pay for a number of coins. The cost of each road is the number inside each diamonds.

You are paying a visit to Ex10si0n island. Can you find the minimum cost for travelling between arbitary two towns?

You may notice that A town is marked in red. The red color have no meanings in current problem.

![](./assets/map.jpg)

**Graph data**

```python
_map = {}
for i in range(7): _map[i] = chr(i+65); _map[chr(i+65)] = i
towns = [chr(i) for i in range(65, 65+7)]
edges = ['A B 4', 'A C 1', 'B C 2', 'B D 7', 'B E 6', 'C E 5',\
         'D G 1', 'E G 6', 'E F 2', 'A F 10', 'F D 9', 'F G 0']

```

### Floyed Warshall

The explanation of Floyed Warshall Algorithm is a little bit complicated in Wiki. From my perspective and understanding, this algorithm is quite easy to understand, the core code is relaxation (松弛操作) while it is the core code of all kinds of Algorithms applied to Shortest Path problems. For the relaxation, the pseudo code below shows how to implement it.

NB: `dis[a][b]` means the minimum distance between node **A** and node **B**, the `dis[][]` array is initialize by infinity number.

```python
# Relaxation
for (from, to, bridge) in adj:
dis[from][to] = min(
	dis[from][to],    # (O)rigin distance
	adj[from][to],    # (D)irect path
	dis[from][bridge] + dis[bridge][to],    # (B)ridge node path
)
```

That is, for each three distinct node, there are three paths need to be compaired, namely `O`, `D`, and `B`. For each pair of path (or abstract path) to iterate, actually we just need to consider the following question.

![](./assets/map.jpg)

> We go to **B** from **A**. Is the path `A --> B`  shorter or we finding a bridge node **C** and the path `A --> C --> B` shorter?
>
> To make it abstract, for any node **F**, **T**: if there is a bridge node **V** can make the distance shorter, adopt it.
>
> As for `dis[F][T]` records the minimum distance rather than a specific path, that means, we can go to **T** from **F** with minimum distance to walk regardless of which path.
>
> As a result, `dis[from][bridge] + dis[bridge][to]` may not represent the relation of three node like `E -> (F) -> D`. But it can represent `E -> (F -> G) -> D` due to the specific path is omited, we care about the distance instead.

Full code implementation

```python
def add_edge(adj, edge):
    f, r, v = edge.split(' ')
    f = _map[f]; r = _map[r]; v = int(v)
    adj[f][r] = adj[r][f] = v

def floyed(adj):
    n = len(adj)
    dis = [[float('inf') for i in range(n)] for j in range(n)]
    for i in range(n): dis[i][i] = 0
    for bridge_node in range(n):
        for from_node in range(n):
            for to_node in range(n):
                dis[from_node][to_node] = min(
                    dis[from_node][to_node], 
                    adj[from_node][to_node], 
                    dis[from_node][bridge_node] + dis[bridge_node][to_node]
                )
    for i in dis:
        print(i)

if __name__ == '__main__':
    towns = [chr(i) for i in range(65, 65+7)]; _map = {}
    adj = [[float('inf') for i in range(len(towns))] for j in range(len(towns))]
    edges = ['A B 4', 'A C 1', 'B C 2', 'B D 7', 'B E 6', 'C E 5',\
         'D G 1', 'E G 6', 'E F 2', 'A F 10', 'F D 9', 'F G 0']
    for i in range(7): _map[i] = chr(i+65); _map[chr(i+65)] = i
    for edge in edges: add_edge(adj, edge)
    floyed(adj)
```

## Breadth First Search

In the last section you have learned one of the Algorithms to solve the Shortest Path problem. Before I introduced the following **Dijkstra** and **SPFA** Algorithms, it is needed to have some ideas on **Breadth First Search** which is widely applied on many kind of searching problems as well as the following two Shortest Path finding Algorithms.

You may noticed that the name of **Breadth First Search** (abbr. BFS) is similar to the name of DFS. The implementation of the two algorithms is wholey different since DFS adopts **recursion** while BFS adopts methodology of **queue** (remember that it is a data structure introduced below?).

A lively metaphor is that BFS is like flooding (or spread of epidemic) , you can check [this](https://www.youtube.com/watch?v=x-VTfcmrLEQ) Youtube video to see the algorithm animation. 

[![](./assets/bfs-anim.png)](https://www.youtube.com/watch?v=x-VTfcmrLEQ)

We can see that, for nodes in same depth, they are visited at the same time (actually, it have the order, but the node in next depth cannot be visited the same time as current depth).

Here shows the pseudo code.

```python
queue = []
queue.append(start)
visit(start)
while queue not empty:
    this_node = queue.pop()
    # do some stuffs
    for next_node in this_node.childrens:
        if next_node not visited:
            queue.append(next_node)
            visit(next_node)
```

`visit()` is the function to mark a node as visited
`this_node.childrens` means the adjacent node to current node

### Maze Problem II

Adopting BFS in solving Maze Problem is another way of thinking. For the question, please refer to the previous [Maze Problem I](https://github.com/Ex10si0n/MPI-Interest-Group#maze-problem-i). Let us try to implement the maze solver by adopting BFS.

Maze parser code here: (You are free to change the map pattern if you like using [maze.py](./codes/algorithms/maze.py))

```python
maze = '''#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.
          #.#.#. . . . . . . .#. . . . . . . .#. .#.
          #. .#. .#.#.#.#.#. .#.#.#. .#.#.#. .#. .#.
          #. . . .#. . . .#. .#. . . .#. .#. . . .#.
          #.#.#.#.#.#.#. .#. .#. .#.#.#. .#.#.#. .#.
          #. . . . . . . .#. .#. . . .#. . . . . .#.
          #. .#.#.#.#.#.#.#. .#. .#. .#.#.#. .#.#.#.
          #. . . . . . . . . .#. .#. . . .#. . . .#.
          #. .#.#.#.#.#.#.#.#.#.#.#.#.#. .#.#.#. .#.
          #. .#. . . . . . . .#. . . . . .#. .#. .#.
          #. .#.#.#. .#.#.#. .#. .#.#.#.#.#. .#. .#.
          #. . . .#. . . .#. . . .#. . . .#. .#. .#.
          #.#.#. .#.#.#. .#.#.#.#.#. .#. .#. .#. .#.
          #. .#. . . . . .#. . . . . .#. .#. .#. .#.
          #. .#.#.#.#.#.#.#.#.#.#.#. .#. .#. .#. .#.
          #. . . . . .#. . . . . .#. .#. . . .#. .#.
          #. .#.#.#.#.#. .#. .#. .#. .#. .#.#.#. .#.
          #. . . . . .#. .#. .#. . . .#. .#. . . .#.
          #. .#.#.#. .#. .#. .#.#.#.#.#.#.#. .#.#.#.
          #. . . .#. . . .#. . . . . . . . . . .#.#.
          #.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.'''

def maze_parser(maze):
    res = []
    for line in maze.strip().split('\n'):
        line = line.strip().split('.')
        res.append(line)
    return res

if __name__ == '__main__':
    maze = maze_parser(maze)
    start = [1, 1]
    end = [19, 19]
```

#### Sol.

```python
maze = '''#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.
          #.#.#. . . . . . . .#. . . . . . . .#. .#.
          #. .#. .#.#.#.#.#. .#.#.#. .#.#.#. .#. .#.
          #. . . .#. . . .#. .#. . . .#. .#. . . .#.
          #.#.#.#.#.#.#. .#. .#. .#.#.#. .#.#.#. .#.
          #. . . . . . . .#. .#. . . .#. . . . . .#.
          #. .#.#.#.#.#.#.#. .#. .#. .#.#.#. .#.#.#.
          #. . . . . . . . . .#. .#. . . .#. . . .#.
          #. .#.#.#.#.#.#.#.#.#.#.#.#.#. .#.#.#. .#.
          #. .#. . . . . . . .#. . . . . .#. .#. .#.
          #. .#.#.#. .#.#.#. .#. .#.#.#.#.#. .#. .#.
          #. . . .#. . . .#. . . .#. . . .#. .#. .#.
          #.#.#. .#.#.#. .#.#.#.#.#. .#. .#. .#. .#.
          #. .#. . . . . .#. . . . . .#. .#. .#. .#.
          #. .#.#.#.#.#.#.#.#.#.#.#. .#. .#. .#. .#.
          #. . . . . .#. . . . . .#. .#. . . .#. .#.
          #. .#.#.#.#.#. .#. .#. .#. .#. .#.#.#. .#.
          #. . . . . .#. .#. .#. . . .#. .#. . . .#.
          #. .#.#.#. .#. .#. .#.#.#.#.#.#.#. .#.#.#.
          #. . . .#. . . .#. . . . . . . . . . .#.#.
          #.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.'''

def maze_parser(maze):
    res = []
    for line in maze.strip().split('\n'):
        line = line.strip().split('.')
        res.append(line)
    return res

class Search:
    def __init__(self, maze, start, end):
        self.visited = []
        self.maze = maze
        self.start = start
        self.end = end
        self.size = end[0] + 2
        self.move_dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        self.path_map = [[[0, 0] for i in range(self.size)] for j in range(self.size)]
        self.solve()

    def record_path(self, _from, towards):
        x, y = _from[0], _from[1]
        x_dir, y_dir = towards[0], towards[1]
        self.path_map[x][y] = [x_dir, y_dir]

    def move(self, _from, towards):
        return [_from[0] + towards[0], _from[1] + towards[1]]

    def draw_path(self, print_dir=False):
        dir2arrow = {'[0, 0]': ' ', '[-1, 0]': '↑', '[0, -1]': '←', '[1, 0]': '↓', '[0, 1]': '→'}
        for i in range(len(self.path_map)):
            for j in range(len(self.path_map)):
                _dir = self.path_map[i][j]
                arrow = dir2arrow[str(_dir)]
                if arrow != ' ': self.maze[i][j] = '*'
                if print_dir: print(arrow, end=' ')
            if print_dir: print()

    def print_maze(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.maze[i][j], end=' ')
            print()

    def solve(self):
        self.bfs(self.start)
        self.draw_path()
        self.print_maze()

    def bfs(self, start_position):
        queue = []
        queue.append(start_position)
        self.visited.append(start_position)
        while queue:
            now_position = queue.pop()
            if now_position == self.end:
                return True
            for _dir in self.move_dir:
                next_position = self.move(_from=now_position, towards=_dir)
                x = next_position[0]; y = next_position[1]
                if next_position not in self.visited and maze[x][y] != '#':
                    self.record_path(now_position, _dir)
                    queue.append(next_position)
                    self.visited.append(next_position)
        return False
        
if __name__ == '__main__':
    maze = maze_parser(maze)
    start = [1, 1]
    end = [19, 19]
    search = Search(maze, start, end)
```

### LC 733

An image is represented by an `m x n` integer grid `image` where `image[i][j]` represents the pixel value of the image.

You are also given three integers `sr`, `sc`, and `newColor`. You should perform a **flood fill** on the image starting from the pixel `image[sr][sc]`.

To perform a **flood fill**, consider the starting pixel, plus any pixels connected **4-directionally** to the starting pixel of the same color as the starting pixel, plus any pixels connected **4-directionally** to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with `newColor`.

Return *the modified image after performing the flood fill*.

 

**Example 1:**

![img](https://assets.leetcode.com/uploads/2021/06/01/flood1-grid.jpg)

```
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
```

**Example 2:**

```
Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
Output: [[2,2,2],[2,2,2]]
```

 

**Constraints:**

- `m == image.length`
- `n == image[i].length`
- `1 <= m, n <= 50`
- `0 <= image[i][j], newColor < 216`
- `0 <= sr < m`
- `0 <= sc < n`

```java
class Solution {
    public void dfs(int[][] image, int origin, int x, int y, int newColor) {
        if (newColor == origin) return;
        int[] dx = {0, 0, -1, 1};
        int[] dy = {-1, 1, 0, 0};
        image[x][y] = newColor;
        for (int i = 0; i < 4; i++) {
            int new_x = x + dx[i];
            int new_y = y + dy[i];
            if (new_x >= 0 && new_x < image.length && new_y >= 0 && new_y < image[0].length) {
                if (image[new_x][new_y] == origin) dfs(image, origin, new_x, new_y, newColor);
            }
        }
    }
    
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        dfs(image, image[sr][sc], sr, sc, newColor);
        return image;
    }
}
```

### LC 1559

Given a 2D array of characters `grid` of size `m x n`, you need to find if there exists any cycle consisting of the **same value** in `grid`.

A cycle is a path of **length 4 or more** in the grid that starts and ends at the same cell. From a given cell, you can move to one of the cells adjacent to it - in one of the four directions (up, down, left, or right), if it has the **same value** of the current cell.

Also, you cannot move to the cell that you visited in your last move. For example, the cycle `(1, 1) -> (1, 2) -> (1, 1)` is invalid because from `(1, 2)` we visited `(1, 1)` which was the last visited cell.

Return `true` if any cycle of the same value exists in `grid`, otherwise, return `false`.

 

**Example 1:**

**![img](https://assets.leetcode.com/uploads/2020/07/15/1.png)**

```
Input: grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
Output: true
Explanation: There are two valid cycles shown in different colors in the image below:
```

**Example 2:**

**![img](https://assets.leetcode.com/uploads/2020/07/15/22.png)**

```
Input: grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
Output: true
Explanation: There is only one valid cycle highlighted in the image below:
```

**Example 3:**

**![img](https://assets.leetcode.com/uploads/2020/07/15/3.png)**

```
Input: grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
Output: false
```

 

**Constraints:**

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 500`
- `grid` consists only of lowercase English letters.

```java
class Solution {
    
    public static int[][] visited;
    public static int[] dx = {0, -1, 0, 1};
    public static int[] dy = {-1, 0, 1, 0};
    
    public boolean inCircular(char[][] grid, int x, int y, int depth) {
        if (visited[x][y] > 0) return depth - visited[x][y] >= 3;
        visited[x][y] = depth;
        for (int i = 0; i < 4; i++) {
            int new_x = x + dx[i];
            int new_y = y + dy[i];
            if (0 <= new_x && new_x < grid.length && 0 <= new_y && new_y < grid[0].length) {
                if (grid[new_x][new_y] == grid[x][y]) {
                    if(inCircular(grid, new_x, new_y, depth + 1)) return true;
                }
            }
        }
        return false;
    }
    
    public boolean containsCycle(char[][] grid) {
        visited = new int[grid.length][grid[0].length];
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (visited[i][j] == 0) {
                    if (inCircular(grid, i, j, 1)) return true;
                }
            }
        }
        return false;
    }
}
```

