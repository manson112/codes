import sys
import collections
import pprint

def findNation(board, N, M):
    visited = [[False for _ in range(M)] for _ in range(N)]
    c = 1
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0 or visited[i][j]:
                continue
            deq = collections.deque()
            deq.append([i, j])
            visited[i][j] = True
            pprint.pprint(visited)
            while deq:
                a = deq.popleft()
                board[a[0]][a[1]] = c
                for d in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    nxt = [a[0]+d[0], a[1]+d[1]]
                    print(nxt)
                    if nxt[0] < 0 or nxt[0] >= N or nxt[1] < 0 or nxt[1] >= M:
                        continue
                    if board[nxt[0]][nxt[1]] == 0 or visited[nxt[0]][nxt[1]]:
                        continue
                    deq.append(nxt)
                    visited[nxt[0]][nxt[1]] = True
            
            c += 1

N, M = map(int, sys.stdin.readline().split(" "))

m = []
for i in range(N):
    m += [list(map(int, sys.stdin.readline().split(" ")))]

    findNation(m, N, M)

    pprint.pprint(m)


pprint.pprint(m)