# Breadth First Search

In the last section you have learned one of the Algorithms to solve the Shortest Path problem. Before I introduced the following **Dijkstra** and **SPFA** Algorithms, it is needed to have some ideas on **Breadth First Search** which is widely applied on many kind of searching problems as well as the following two Shortest Path finding Algorithms.

You may noticed that the name of **Breadth First Search** (abbr. BFS) is similar to the name of DFS. The implementation of the two algorithms is wholey different since DFS adopts **recursion** while BFS adopts methodology of **queue** (remember that it is a data structure introduced below?).

A lively metaphor is that BFS is like flooding (or spread of epidemic) , you can check [this](https://www.youtube.com/watch?v=x-VTfcmrLEQ) Youtube video to see the algorithm animation.

[![](../../assets/bfs-anim.png)](https://www.youtube.com/watch?v=x-VTfcmrLEQ)

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

`visit()` is the function to mark a node as visited `this_node.childrens` means the adjacent node to current node

### Maze Problem II

Adopting BFS in solving Maze Problem is another way of thinking. For the question, please refer to the previous [Maze Problem I](https://github.com/Ex10si0n/MPI-Interest-Group#maze-problem-i). Let us try to implement the maze solver by adopting BFS.

Maze parser code here: (You are free to change the map pattern if you like using [maze.py](../codes/algorithms/maze.py))

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

Return _the modified image after performing the flood fill_.

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

* `m == image.length`
* `n == image[i].length`
* `1 <= m, n <= 50`
* `0 <= image[i][j], newColor < 216`
* `0 <= sr < m`
* `0 <= sc < n`

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

![img](https://assets.leetcode.com/uploads/2020/07/15/1.png)

```
Input: grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
Output: true
Explanation: There are two valid cycles shown in different colors in the image below:
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2020/07/15/22.png)

```
Input: grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
Output: true
Explanation: There is only one valid cycle highlighted in the image below:
```

**Example 3:**

![img](https://assets.leetcode.com/uploads/2020/07/15/3.png)

```
Input: grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
Output: false
```

**Constraints:**

* `m == grid.length`
* `n == grid[i].length`
* `1 <= m, n <= 500`
* `grid` consists only of lowercase English letters.

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
