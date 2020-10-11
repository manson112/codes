import sys
sys.setrecursionlimit(10000)
M, N = map(int, sys.stdin.readline().split(" "))
board = []
board += [[10001 for _ in range(N+1)]]
for i in range(M):
    board += [[10001] + list(map(int, sys.stdin.readline().split(" ")))]
dp = [[-1 for _ in range(N+1)] for _ in range(M+1)]
def dfs(x, y):
    global board, dp, M, N
    if x == M and y == N :
        return 1
    if dp[x][y] == -1:
        dp[x][y] = 0
        for d in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nxtX = x + d[0]
            nxtY = y + d[1]
            if nxtX <= 0 or nxtX >= M+1 or nxtY <= 0 or nxtY >= N+1:
                continue
            if board[nxtX][nxtY] >= board[x][y]:
                continue
            dp[x][y] += dfs(nxtX, nxtY)
    return dp[x][y]

print(dfs(1,1))