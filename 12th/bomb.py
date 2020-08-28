import sys
import pprint

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

(R, C, N) = (map(int, sys.stdin.readline().split(" ")))

m = []
initaialState = []
for i in range(R) :
    line = sys.stdin.readline().rstrip()
    initaialState += [line]
    m += [[0 if c == '.' else 2 for c in line]]

if N < 2 :
    for i in range(R):
        print(initaialState[i])
else :
    for t in range(2, N) :
        bombed = [[False for _ in range(C)] for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if not bombed[i][j]:
                    m[i][j] += 1
                if m[i][j] == 3:
                    m[i][j] = -1
                    bombed[i][j] = True
                    for d in range(4):
                        nxtX = i + dx[d]
                        nxtY = j + dy[d]
                        if 0 <= nxtX < R and 0 <= nxtY < C :
                            if m[nxtX][nxtY] != 2 :
                                m[nxtX][nxtY] = -1
                                bombed[nxtX][nxtY] = True
    for i in range(R):
        for j in range(C):
            if m[i][j] == -1:
                print(".",end='')
            else:
                print("O",end='')
        print()


