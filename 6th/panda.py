

n = int(input())

mmap = []
loc = [[0,0] for i in range(n*n)]
result = [[1 for i in range(n)] for j in range(n)]
for i in range(n):
    line = input().rstrip().split(" ")
    tmp = []
    for j in range(n):
        tmp += [int(line[j])]
        loc[int(line[j])-1] = [i, j]
    mmap += tmp

for i in range(n*n):
    location = loc[i]
    
    m = 10000000

    for d in enumerate([[1, 0], [0, 1], [-1, 0], [0, -1]]):
        newX = location[0] + d[0]
        newY = location[1] + d[1]
        if newX < 0 or newX >= len(n) or newY < 0 or newY >= len(n) :
            continue
        if mmap[newX][newY] < m:
            m = mmap[newX][newY]

        
        
        
        
