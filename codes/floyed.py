towns = [chr(i) for i in range(65, 65+7)]
_map = {}
for i in range(7): _map[i] = chr(i+65); _map[chr(i+65)] = i