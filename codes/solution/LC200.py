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
