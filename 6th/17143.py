import pprint, copy
directions = [(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)]
count = 0
def catch(mmap, speed, direction, size, shark, current) :
    global count
    for i in range(1, len(mmap)):
        if mmap[i][current] != -1:
            count += size[mmap[i][current]]
            shark[mmap[i][current]] = [-1, -1]
            mmap[i][current] = -1
            break
    
def move(mmap, nextMap, speed, direction, size, shark) :
    global directions
    for i in range(len(shark)):
        if shark[i][0] != -1 and shark[i][1] != -1:
            sharkNum = mmap[shark[i][0]][shark[i][1]]
            d = direction[sharkNum]

            for j in range(speed[sharkNum]):
                if d == 1 or d == 2:
                    if shark[i][0] + directions[d][0] == 0 or shark[i][0] + directions[d][0] == len(mmap) :
                        d = 3 - d
                else:
                    if shark[i][1] + directions[d][1] == 0 or shark[i][1] + directions[d][1] == len(mmap[0]) :
                        d = 7 - d
                if j == speed[sharkNum]-1:
                    spot = nextMap[shark[i][0] + directions[d][0]][shark[i][1] + directions[d][1]]
                    if spot != -1:
                        if size[spot] > size[i] :
                            shark[i] = [-1, -1]
                        else :
                            shark[spot] = [-1, -1]
                            shark[i][0] += directions[d][0]
                            shark[i][1] += directions[d][1]
                        break
                shark[i][0] += directions[d][0]
                shark[i][1] += directions[d][1]
            direction[sharkNum] = d
            nextMap[shark[i][0]][shark[i][1]] = i

line = input().rstrip().split(" ")

row, column, m = int(line[0]), int(line[1]), int(line[2])

speed = [0] * m 
direction = [0] * m
size = [0] * m
shark = [(-1, -1)] * m

mmap = [[-1 for _ in range(column+1)] for _ in range(row+1)]


for i in range(m):
    l = input().rstrip().split(" ")
    r, c, s, d, z = int(l[0]), int(l[1]), int(l[2]), int(l[3]), int(l[4])
    shark[i] = [r, c]
    speed[i] = s
    direction[i] = d
    size[i] = z
    mmap[r][c] = i

for cur in range(1, column+1):
    catch(mmap, speed, direction, size, shark, cur)
    nextMap = [[-1 for _ in range(column+1)] for _ in range(row+1)]
    move(mmap, nextMap, speed, direction, size, shark)
    mmap = nextMap[:]

print(count)