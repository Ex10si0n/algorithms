G = {}
    
input_data = '''A B
                A E
                A G
                E F
                F G
                E C
                C F
                G D
                C D
                B G'''

data = input_data.split()

for i in range(10):    # The above graph has 10 edges
    from_node, to_node = data[i * 2], data[i * 2 + 1]
    if from_node in G.keys(): G[from_node].append(to_node)
    else: G[from_node] = [to_node]
    if to_node in G.keys(): G[to_node].append(from_node)
    else: G[to_node] = [from_node]

print(G)
