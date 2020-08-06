import sys
import pprint
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
done = set()
N, M, F = map(int, sys.stdin.readline().split())
board= [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
taxi = list(map(int, sys.stdin.readline().split()))
taxi[0] -= 1
taxi[1] -= 1

dp = [[[999999 for _ in range(len(board))] for _ in range(len(board))] for _ in range(M)]

passenger = []
for i in range(M):
    passenger += [list(map(int, sys.stdin.readline().split()))]
    passenger[i][0] -= 1
    passenger[i][1] -= 1
    passenger[i][2] -= 1
    passenger[i][3] -= 1

def makeMap(index, psg) :
    global dp, board
    Q = [[psg[0], psg[1], 0]]
    dp[index][psg[0]][psg[1]] = 0
    score = 1
    while len(Q) != 0 :
        A = Q.pop(0)
        for i in range(4):
            nxt = [A[0] + dx[i], A[1] + dy[i], A[2] + 1]
            if 0 <= nxt[0] < len(board) and  0 <= nxt[1] < len(board):
                if board[nxt[0]][nxt[1]] == 1:
                    continue
                if dp[index][nxt[0]][nxt[1]] > nxt[2]:
                    dp[index][nxt[0]][nxt[1]] = nxt[2]
                    Q += [nxt]
        score += 1

def findPassenger():
    global dp, done, M, taxi, passenger
    idx = 404
    dist = 99999999
    for i in range(M):
        if i in done:
            continue
        taxiToP = dp[i][taxi[0]][taxi[1]]
        if taxiToP == dist:
            if passenger[i][0] < passenger[idx][0]:
                idx = i
                dist = taxiToP
            elif passenger[i][0] == passenger[idx][0] and passenger[i][1] < passenger[idx][1]:
                idx = i
                dist = taxiToP
        elif taxiToP < dist:
            dist = taxiToP
            idx = i
    done.add(idx)
    return idx, dist

for i in range(M):
    makeMap(i, passenger[i])

while len(done) < M:
    mIndex, m = findPassenger()
    pToDest = dp[mIndex][passenger[mIndex][2]][passenger[mIndex][3]]
    if pToDest == 999999 or F <= 0 or F <= m or F < m + pToDest:
        F = -1
        break
    F = F - m - pToDest + 2*pToDest
    taxi = [passenger[mIndex][2], passenger[mIndex][3]]

print(F)