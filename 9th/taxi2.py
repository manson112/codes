import sys
import pprint
import collections
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
done = set()
N, M, F = map(int, sys.stdin.readline().split())
board= [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
taxi = list(map(int, sys.stdin.readline().split()))
taxi[0] -= 1
taxi[1] -= 1

passenger = []
for i in range(M):
    passenger += [list(map(int, sys.stdin.readline().split()))]
    passenger[i][0] -= 1
    passenger[i][1] -= 1
    passenger[i][2] -= 1
    passenger[i][3] -= 1
    board[passenger[i][0]][passenger[i][1]] = (i+1)*10

def selectPassenger(taxi, passengers):
    global dx, dy, N, board
    start = (taxi[0], taxi[1])
    print(start)
    q = collections.deque([])
    q.append((taxi[0], taxi[1], 0))
    visited = [[0 for _ in range(N)] for _ in range(N)]
    
    dist = 999999
    ps = []

    while q:
        a = q.popleft()
        if visited[a[0]][a[1]] != 0:
            if visited[a[0]][a[1]] > a[2]:
                visiteid[a[0]][a[1]] = a[2]
            continue
        
        if a[0] == taxi[0] and a[1] == taxi[1] and a[2] != 0:
            continue

        visited[a[0]][a[1]] = a[2]
        
        if a[2]>dist:
            break

        if board[a[0]][a[1]] > 9:
            if len(ps) == 0:
                ps.append(a)
                dist = a[2]
            else:
                ps.append(a)

        
        for i in range(4):
            nxtX = a[0] + dx[i]
            nxtY = a[1] + dy[i]
            if nxtX < 0 or nxtX >= N or nxtY < 0 or nxtY >= N:
                continue
            if board[nxtX][nxtY] == 1:
                continue
            q.append((nxtX, nxtY, a[2]+1))

    print(ps)
    
    selectedIndex = 0
    selectedDistance = 9999999
    for i in range(len(ps)):
        print(i, selectedIndex, selectedDistance)
        if ps[i][2] < selectedDistance:
            selectedIndex = board[ps[i][0]][ps[i][1]] // 10 - 1
            selectedDistance = ps[i][2]
        elif ps[i][2] == selectedDistance:
            if ps[i][0] < passengers[selectedIndex][0]:
                selectedIndex = board[ps[i][0]][ps[i][1]] // 10 - 1
            elif ps[i][0] == passengers[selectedIndex][0]:
                if ps[i][1] < passengers[selectedIndex][1]:
                    selectedIndex = board[ps[i][0]][ps[i][1]] // 10 - 1

    
    print(selectedIndex, selectedDistance)
    
    return selectedIndex, selectedDistance

def getDist(p):
    global dx, dy, N, board

    q = collections.deque([])
    q.append((p[0], p[1], 0))
    visited = [[0 for _ in range(N)] for _ in range(N)]

    while q:
        a = q.popleft()
        if visited[a[0]][a[1]] != 0:
            if visited[a[0]][a[1]] > a[2]:
                visiteid[a[0]][a[1]] = a[2]
            continue

        if a[0] == p[0] and a[1] == p[1] and a[2] != 0:
            continue
        
        visited[a[0]][a[1]] = a[2]

        if a[0] == p[2] and a[1] == p[3]:
            return a[2]

        for i in range(4):
            nxtX = a[0] + dx[i]
            nxtY = a[1] + dy[i]
            if nxtX < 0 or nxtX >= N or nxtY < 0 or nxtY >= N:
                continue
            if board[nxtX][nxtY] == 1:
                continue
            q.append((nxtX, nxtY, a[2]+1))

    return -1

flg = True
while passenger:
    pprint.pprint(board)
    print(passenger)
    i, d = selectPassenger(taxi, passenger)
    if d > F:
        flg = False
        break
    F -= d
    dist = getDist(passenger[i])
    if dist == -1 or dist > F:
        flg = False
        break

    F = F - d - dist + dist*2

    board[passenger[i][0]][passenger[i][1]] = 0
    taxi = (passenger[i][2],passenger[i][3])

    passenger.pop(i)

if flg:
    print(F)
else:
    print(-1)
    
    