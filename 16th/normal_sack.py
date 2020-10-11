import sys

N, K = map(int, sys.stdin.readline().split(" "))
# w, v
stuffs = []
for i in range(N):
    w, v = map(int, sys.stdin.readline().split(" "))
    stuffs += [[w, v]]
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(K+1) :
        if j < stuffs[i-1][0]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-stuffs[i-1][0]]+stuffs[i-1][1])
print(dp[N][K])
