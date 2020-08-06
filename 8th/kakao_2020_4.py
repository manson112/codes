# 2개 시간초과
import json
import sys 
sys.setrecursionlimit(10**8)

dx = [0, 1, 0, -1]
dy = [1, 0, -1 , 0]
dp = [[]]
m = 9999999

def dfs(depth, board, visited, cur, cost, dir):
    global dx, dy, m, dp
    if board[cur[0]][cur[1]] == 1:
        return
    if visited[cur[0]][cur[1]]:
        return
    
    if cur == [len(board)-1, len(board)-1]:
        m = min(m, cost)
        return

    visited[cur[0]][cur[1]] = True
    dp[cur[0]][cur[1]] = cost

    for i in range(4):
        nxt = [cur[0] + dx[i], cur[1] + dy[i]]
        nxtCost = cost
        if (dir == 0 and i == 2) or (dir == 1 and i == 3) or (dir == 2 and i == 0) or (dir == 3 and i == 1):
            continue
        if nxt[0] < 0 or nxt[0] >= len(board) or nxt[1] < 0 or nxt[1] >= len(board):
            continue

        if dir == i :
            nxtCost += 100
        else :
            nxtCost += 600

        if board[nxt[0]][nxt[1]] == 1:
            continue
        if dp[nxt[0]][nxt[1]] < nxtCost :
            continue

        if nxtCost >= m:
            continue

        dfs(depth+1, board, json.loads(json.dumps(visited)), nxt, nxtCost, i)

def dfsWrapper(board):
    global m, dp
    visited = [[False for _ in range(len(board))] for _ in range(len(board))]
    visited[0][0] = True
    m = 9999999
    dp = [[9999999 for _ in range(len(board))] for _ in range(len(board))]
    dp[0][0] = 0
    dfs(0, board, json.loads(json.dumps(visited)), [0, 1], 100, 0)
    dfs(0, board, json.loads(json.dumps(visited)), [1, 0], 100, 1)

def solution(board):
    global m
    dfsWrapper(board)
    return m


print(solution([[0,0,0],[0,0,0],[0,0,0]]))
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))