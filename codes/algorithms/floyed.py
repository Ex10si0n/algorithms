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
