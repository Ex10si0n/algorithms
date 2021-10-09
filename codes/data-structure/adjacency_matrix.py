edges = ['A B', 'B E', 'B C', 'E C', 'E D', 'C D', 'E F']
_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5,\
         5: 'F', 4: 'E', 3: 'D', 2: 'C', 1: 'B', 0: 'A'}

adj = []
n = len(edges)


for i in range(n):
    adj.append([0] * n)

for e in edges:
    from_node, to_node = e.split(' ')
    adj[_map[from_node]][_map[to_node]] = adj[_map[to_node]][_map[from_node]] = 1

for i in range(n):
    for j in range(i, n):
        if adj[i][j] == 1:
            print(_map[i], '---', _map[j])