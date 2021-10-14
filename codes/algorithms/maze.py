'''
This is a Generator of random maze with DFS Algorithm, plus, it has dfs-solver
designed for the maze. You can change the Pereference Settings Block below to see 
different results.
'''
import random

'''
Pereference Settings
'''
display_answer = True
display_maze = True
usr_input_scale = False
display_trace = True
scale_x = 10
scale_y = 10
'''
Algorithm
'''

if usr_input_scale:
	scale_x = int(input("scale_x: "))
	scale_y = int(input("scale_y: "))

vis = [[0 for col in range(scale_y + 1)] for row in range(scale_x + 1)]
maze = [['▇' for col in range(2 * scale_y + 1)] for row in range(2 * scale_x + 1)]
sol = [[0 for col in range(2 * scale_y + 1)] for row in range(2 * scale_x + 1)]
dir_x = [0, -1, 0, 1]
dir_y = [1, 0, -1, 0]
shuf = [0, 1, 2, 3]
flag = 0
trac = []
ans = []

def init():
	for i in range(1, 2 * scale_x + 1, 2):
		for j in range(1, 2 * scale_y + 1, 2):
			maze[i][j] = ' '
	gen_maze(0, 0)
	if display_maze:
		print_maze(maze)
	solver(1, 1)
	if display_trace:
		for i in range(1, scale_x * 2):
			for j in range(1, scale_y * 2):
				if(maze[i][j] != ' ' and maze[i][j] != '▇'):
					if(maze[i - 1][j] != ' ' and maze[i - 1][j] != '▇' and maze[i + 1][j] != ' ' and maze[i + 1][j] != '▇'):
						maze[i][j] = '│'
					if(maze[i][j - 1] != ' ' and maze[i][j - 1] != '▇' and maze[i][j + 1] != ' ' and maze[i][j + 1] != '▇'):
						maze[i][j] = '─'
					if(maze[i][j + 1] != ' ' and maze[i][j + 1] != '▇' and maze[i - 1][j] != ' ' and maze[i - 1][j] != '▇'):
						maze[i][j] = '└'
					if(maze[i][j - 1] != ' ' and maze[i][j - 1] != '▇' and maze[i + 1][j] != ' ' and maze[i + 1][j] != '▇'):
						maze[i][j] = '┐'
					if(maze[i][j + 1] != ' ' and maze[i][j + 1] != '▇' and maze[i + 1][j] != ' ' and maze[i + 1][j] != '▇'):
						maze[i][j] = '┌'
					if(maze[i][j - 1] != ' ' and maze[i][j - 1] != '▇' and maze[i - 1][j] != ' ' and maze[i - 1][j] != '▇'):
						maze[i][j] = '┘'
	if display_answer:
		print()
		print_maze(maze)

def print_maze(x):
	for i in x:
		for j in i:
			print(j, end = '.')
		print()

def gen_maze(now_x, now_y):
	shuf = [0, 1, 2, 3]
	vis[now_x][now_y] = 1
	random.shuffle(shuf)
	for i in shuf:
		new_x, new_y = now_x + dir_x[i], now_y + dir_y[i]
		if new_x < 0 or new_x >= scale_x or new_y < 0 or new_y >= scale_y:
			pass
		else:
			if not vis[new_x][new_y]:
				maze[2 * now_x + 1 + dir_x[i]][2 * now_y + 1 + dir_y[i]] = ' '
				gen_maze(new_x, new_y)

def solver(now_x, now_y):
	trac.append([now_x, now_y])
	sol[now_x][now_y] = 1
	if now_x == scale_x * 2 - 1 and now_y == scale_y * 2 - 1:
		ans = trac[:]
		while ans:
			t = ans.pop(0)
			maze[t[0]][t[1]] = '•'
	for i in range(4):
		new_x, new_y = now_x + dir_x[i], now_y + dir_y[i]
		if maze[new_x][new_y] == '▇':
			pass
		else:
			if not sol[new_x][new_y]:
				solver(new_x, new_y)
				trac.pop()
	return

init()
