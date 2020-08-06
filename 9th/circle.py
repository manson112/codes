import sys
import collections
import pprint

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def rotate(c, count, direction):
    if direction == 0:
        # 시계방향 [1, 1, 2, 3] => [3, 1, 1, 2]
        for i in range(count):
            c.appendleft(c.pop())
    else:
        # 반시계방향 [1, 1, 2, 3] => [1, 2, 3, 1]
        for i in range(count):
            c.append(c.popleft())

def remove(board, n, m):
    global dx, dy
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                continue
            visited = [[False for _ in range(m)] for _ in range(n)]
            q = collections.deque()
            q.append((i, j, board[i][j]))
            l = set()
            
            while q:
                a = q.popleft()

                visited[a[0]][a[1]] = True
                print(a)
                pprint.pprint(visited)
                for d in range(4):
                    nxtX = a[0] + dx[d]
                    nxtY = a[1] + dx[d]
                    if nxtX < 0 or nxtX >= n or nxtY < 0 or nxtY >= m:
                        continue
                    if board[nxtX][nxtY] != a[2]:
                        continue
                    if not visited[nxtX][nxtY] and board[nxtX][nxtY] != 0:
                        l.add((nxtX, nxtY, a[2]))
                        l.add((a[0], a[1], a[2]))
                        q.append((nxtX, nxtY, a[2]))

            check = [False for _ in range(n)]
            for a in l:
                board[a[0]][a[1]] = 0
                check[a[0]] = True

            for t in range(len(check)):
                if not check[t]:
                    s = 0
                    count = 0
                    for ind in range(m):
                        if board[t][ind] != 0:
                            count += 1
                            s += board[t][ind]
                    average = s / count
                    for ind in range(m):
                        if board[t][ind] != 0:
                            if board[t][ind] > average:
                                board[t][ind] -= 1
                            elif board[t][ind] < average:
                                board[t][ind] += 1


firstLine = list(map(int, sys.stdin.readline().split()))
N, M, T = firstLine[0], firstLine[1], firstLine[2]

board = []

for i in range(N):
    board += [collections.deque(list(map(int, sys.stdin.readline().split())))]

pprint.pprint(board)

for i in range(T):
    (x, d, k) = tuple(list(map(int, sys.stdin.readline().split())))
    
    # M의 배수 인 경우 
    if k % M == 0 : continue
    
    # 회전
    for j in range(x-1, len(board), x):
        rotate(board[j], k, d)

    pprint.pprint(board)
    remove(board, N, M)    
    pprint.pprint(board)



                
s = 0
for i in range(N):
    for j in range(M):
        s += board[i][j]

    
print(s)