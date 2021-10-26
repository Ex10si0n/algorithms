height = [1, 8, 6, 2, 5, 4, 8, 3, 7] 

max_size = 0

for i in range(len(height)):
    for j in range(i, len(height)):
        width = j - i
        shorter = min(height[i], height[j])
        max_size = max(width * shorter, max_size)

print(max_size)


