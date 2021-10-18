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
                if next_position not in self.visited and maze[x][y] != '▇':
                    self.record_path(now_position, _dir)
                    queue.append(next_position)
                    self.visited.append(next_position)
        return False
        
if __name__ == '__main__':
    maze = maze_parser(maze)
    start = [1, 1]
    end = [19, 19]
    search = Search(maze, start, end)
