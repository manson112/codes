import sys
import collections
import json
import pprint

N, M = map(int, sys.stdin.readline().split(" "))
m = []
for i in range(N):
    m += [list(map(int, sys.stdin.readline().rstrip().split(" ")))]

cheese = []
for i in range(N):
    for j in range(1, M):
        if m[i][j] != 0:
            cheese += [[i, j]]

t = 0
goneList = []

while cheese:
    tmpMap = json.loads(json.dumps(m))
    for g in goneList:
        tmpMap[g[0]][g[1]] = 0
        cheese.remove(g)
    m = json.loads(json.dumps(tmpMap))
    goneList = []

    air = 2
    deq = collections.deque()
    visited = [[False for _ in range(M)] for _ in range(N)]
    deq.append([0, 0])
    visited[0][0] = True
    tmpMap[0][0] = air
    
    while deq :
        a = deq.popleft()
        for d in [[0, -1], [-1, 0], [0, 1], [1, 0]]:
            nxt = [a[0]+d[0], a[1]+d[1]]
            if 0 <= nxt[0] < N and 0 <= nxt[1] < M:
                if tmpMap[nxt[0]][nxt[1]] == 0 and not visited[nxt[0]][nxt[1]]:
                    deq.append(nxt)
                    visited[nxt[0]][nxt[1]] = True
                    tmpMap[nxt[0]][nxt[1]] = air

    for c in cheese :
        count = 0
        for d in [[0, -1], [-1, 0], [0, 1], [1, 0]]:
            nxt = [c[0]+d[0], c[1]+d[1]]
            if 0 <= nxt[0] < N and 0 <= nxt[1] < M:
                if tmpMap[nxt[0]][nxt[1]] == 2:
                    count += 1
        if count >= 2:
            goneList += [c]

    t += 1
    
print(t-1)

