maze = '''▇.▇.▇.▇.▇.▇.▇.▇.▇.▇.▇.▇.▇.▇.▇.▇.▇.▇.▇.▇.▇.
          ▇.#.▇. . . . . . . .▇. . . . . . . .▇. .▇.
          ▇. .▇. .▇.▇.▇.▇.▇. .▇.▇.▇. .▇.▇.▇. .▇. .▇.
          ▇. . . .▇. . . .▇. .▇. . . .▇. .▇. . . .▇.
          ▇.▇.▇.▇.▇.▇.▇. .▇. .▇. .▇.▇.▇. .▇.▇.▇. .▇.
          ▇. . . . . . . .▇. .▇. . . .▇. . . . . .▇.
          ▇. .▇.▇.▇.▇.▇.▇.▇. .▇. .▇. .▇.▇.▇. .▇.▇.▇.
          ▇. . . . . . . . . .▇. .▇. . . .▇. . . .▇.
          ▇. .▇.▇.▇.▇.▇.▇.▇.▇.▇.▇.▇.▇.▇. .▇.▇.▇. .▇.
          ▇. .▇. . . . . . . .▇. . . . . .▇. .▇. .▇.
          ▇. .▇.▇.▇. .▇.▇.▇. .▇. .▇.▇.▇.▇.▇. .▇. .▇.
          ▇. . . .▇. . . .▇. . . .▇. . . .▇. .▇. .▇.
          ▇.▇.▇. .▇.▇.▇. .▇.▇.▇.▇.▇. .▇. .▇. .▇. .▇.
          ▇. .▇. . . . . .▇. . . . . .▇. .▇. .▇. .▇.
          ▇. .▇.▇.▇.▇.▇.▇.▇.▇.▇.▇.▇. .▇. .▇. .▇. .▇.
          ▇. . . . . .▇. . . . . .▇. .▇. . . .▇. .▇.
          ▇. .▇.▇.▇.▇.▇. .▇. .▇. .▇. .▇. .▇.▇.▇. .▇.
          ▇. . . . . .▇. .▇. .▇. . . .▇. .▇. . . .▇.
          ▇. .▇.▇.▇. .▇. .▇. .▇.▇.▇.▇.▇.▇.▇. .▇.▇.▇.
          ▇. . . .▇. . . .▇. . . . . . . . . . .#.▇.
          ▇.▇.▇.▇.▇.▇.▇.▇.▇.▇.▇.▇.▇.▇.▇.▇.▇.▇.▇.▇.▇.'''

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
            if next_position not in self.visited and maze[x][y] != '▇':
                self.dfs(next_position, path+now_position)
        return False


if __name__ == '__main__':
    maze = maze_parser(maze)
    start = [1, 1]
    end = [19, 19]
    search = Search(maze, start, end)
