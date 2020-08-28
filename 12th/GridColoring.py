import sys
import pprint
import json
sys.setrecursionlimit(1500)
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
(M, N) = map(int, sys.stdin.readline().split(" "))
result = []
def check(m, s, c):
    global M, N, dx, dy

    if c == 'B' :
        for i in range(2):
            nxtX = s[0] + dx[i]
            nxtY = s[1] + dy[i]
            if 0 <= nxtX < M and 0 <= nxtY < N:
                if m[nxtX][nxtY] == 'R':
                    return False
    else : 
        for i in range(2, 4):
            nxtX = s[0] + dx[i]
            nxtY = s[1] + dy[i]
            if 0 <= nxtX < M and 0 <= nxtY < N:
                if m[nxtX][nxtY] == 'B':
                    return False
    return True

def dfs(m, spaces, i, path):
    global result
    if i >= len(spaces):
        result += [path]
        return
    m[spaces[i][0]][spaces[i][1]] = 'B'
    if check(m, spaces[i], 'B') :
        tmp = json.loads(json.dumps(path))
        tmp += ['B']
        dfs(m, spaces, i+1, tmp)
    m[spaces[i][0]][spaces[i][1]] = 'R'
    if check(m, spaces[i], 'R') :
        tmp = json.loads(json.dumps(path))
        tmp += ['R']
        dfs(m, spaces, i+1, tmp)
    m[spaces[i][0]][spaces[i][1]] = '.'

m = []
blues = []
reds = []
spaces = []
count = 0

for i in range(M):
    line = sys.stdin.readline().rstrip()
    l = []
    for j, c in enumerate(line):
        if c == 'B':
            for b in blues:
                if b[0] < i and b[1] < j:
                    blues.remove(b)
            blues += [(i, j)]
        elif c == 'R':
            f = True
            for r in reds:
                if r[0] < i and r[1] < j:
                    f = False
            if f :
                reds += [(i, j)]
        else :
            count += 1
        l += [c]
    m += [l]
    
flg = True
for b in blues:
    for i in range(b[0], -1, -1):
        for j in range(b[1], -1, -1):
            if m[i][j] == 'R':
                flg = False
                print(0)
                break
            m[i][j] = 'B'
        if not flg:
            break
    if not flg:
        break  
if count == 0:
    flg = False
    print(1)
if flg :
    for r in reds:
        for i in range(r[0], M):
            for j in range(r[1], N):
                m[i][j] = 'R'
    
    for i in range(M):
        for j in range(N):
            if m[i][j] == '.':
                spaces += [(i, j)]
    dfs(m, spaces, 0, [])        
    print(len(set(tuple(i) for i in result)))