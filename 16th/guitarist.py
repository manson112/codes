import sys
r = lambda: map(int, sys.stdin.readline().split(" "))
N, S, M = r()
vol = list(r())
dp = [[0 for _ in range(M+1)] for _ in range(N)]

if S + vol[0] <= M: 
    dp[0][S + vol[0]] = 1
if S - vol[0] >= 0:
    dp[0][S - vol[0]] = 1

for i in range(1, N):
    prev = i-1
    for j in range(M+1):
        if dp[prev][j] == 1:
            if j + vol[i] <= M :
                dp[i][j+vol[i]] = 1
            if j - vol[i] >= 0 :
                dp[i][j-vol[i]] = 1

if sum(dp[-1]) == 0:
    print(-1)
else:
    for i in range(len(dp[-1])-1, -1, -1):
        if dp[-1][i] == 1:
            print(i)
            break