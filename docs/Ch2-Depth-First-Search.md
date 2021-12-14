# Chapter 2. Graph Theory


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
