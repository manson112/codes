import sys
import pprint
import json
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

loc = [(0,0) for _ in range(17)]
direction = [0] * 17

m = [[0 for _ in range(6)] for _ in range(6)]

for i in range(4):
    line = list(map(int, sys.stdin.readline().split()))
    for j in range(4):
        one = line[j * 2]
        two = line[j * 2 + 1]
        loc[one] = (i+1, j+1)
        direction[one] = two
        m[i+1][j+1] = one

finished = False

s = m[1][1]
direction[0] = direction[s]
loc[0] = (1, 1)
loc[s] = (-1, -1)
m[1][1] = 0

res = 0

def move_fish(m) :
    global loc, direction, dx, dy
    for i in range(1, 17):
        # dead fish
        if loc[i] == (-1, -1):
            continue
        tmpDirection = direction[i]
        nxt = (loc[i][0] + dx[direction[i]], loc[i][1] + dy[direction[i]])
        # change direction
        while m[nxt[0]][nxt[1]] == 0:
            direction[i] = (direction[i] + 1) % 8
            nxt = (loc[i][0] + dx[direction[i]], loc[i][1] + dy[direction[i]])
        if direction[i] == 0:
            direction[i] = tmpDirection
        else :
            tmp = m[nxt[0]][nxt[1]]
            # swap
            m[loc[i][0]][loc[i][1]], m[nxt[0]][nxt[1]] = m[nxt[0]][nxt[1]], m[loc[i][0]][loc[i][1]]
            if tmp == -1:
                loc[i] = nxt
            else:
                loc[i], loc[tmp] = nxt, loc[i]


def move_shark(step, dist, m, loc, direction, curSum):
    global dx, dy, res
    nxt = (loc[0][0] + dx[direction[0]] * dist, loc[0][1] + dy[direction[0]] * dist)
    print("NEXT:", nxt)
    if nxt[0] <= 0 or nxt[0] >= 5 or nxt[1] <= 0 or nxt[1] >= 5:
        res = max(res, curSum)
        return 
    

    tmp = m[nxt[0]][nxt[1]]
    print("TMP: ", tmp)
    print(loc[tmp])
    print(direction)
    # empty
    if tmp == -1 or m[nxt[0]][nxt[1]] == 0:
        res = max(res, curSum)
        return
    # eat
    curSum += tmp
    direction[0] = direction[tmp]
    m[loc[0][0]][loc[0][1]] = -1
    m[loc[tmp][0]][loc[tmp][1]] = 0
    loc[0] = nxt
    loc[tmp] = (-1, -1)

    print("after move")
    pprint.pprint(m)
    solve(step+1, json.loads(json.dumps(m)), json.loads(json.dumps(loc)), json.loads(json.dumps(direction)), curSum)

def solve(step, curMap, loc, direction, curSum):
    move_fish(json.loads(json.dumps(curMap)))
    for i in range(1, 4):
        print("[", step, "]i = ", i)
        print("before move")
        pprint.pprint(curMap)
        print("direction: ", direction[0])
        print()
        print()
        move_shark(step, i, json.loads(json.dumps(curMap)),json.loads(json.dumps(loc)), json.loads(json.dumps(direction)), curSum)

solve(0, m, loc, direction, s)

print(res)