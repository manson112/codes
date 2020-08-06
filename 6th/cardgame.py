import sys
sys.setrecursionlimit(1000000)

dp = [[-1 for i in range(2002)] for j in range(2002)]
l = []
r = []

def solve(n, m):
    global dp, l, r
    if n <= 0 or m <= 0: return 0
    if dp[n][m] != -1: return dp[n][m]

    res = 0
    if l[n-1] > r[m-1] : 
        res = max(res, solve(n, m-1) + r[m-1])
    res = max(res, solve(n-1,m-1))
    res = max(res, solve(n-1,m))
    dp[n][m] = res
    return res

def solution(left, right):
    global l, r
    l = left
    r = right
    return solve(len(left), len(right))


print(solution([2,2,3], [2,2,3]))