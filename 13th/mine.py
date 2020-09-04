import collections
color = 1

def fillNumbers(board, coloredMap) :
    global color
    zeros = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != "*":
                mine = 0
                a = [i, j]
                for d in [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]] :
                    nxt = [a[0] + d[0], a[1] + d[1]]
                    if nxt[0] < 0 or nxt[0] >= len(board) or nxt[1] < 0 or nxt[1] >= len(board):
                        continue
                    if board[nxt[0]][nxt[1]] == '*':
                        mine += 1
                board[a[0]][a[1]] = mine    

                if mine == 0:
                    zeros += [a]  

    if len(zeros) == 0:
        return

    deq = collections.deque()
    visited = [[False for _ in range(len(board))] for _ in range(len(board))]
    deq.append(zeros[0])
    visited[zeros[0][0]][zeros[0][1]] = True

    while deq:
        a = deq.popleft()
        c = color
        if coloredMap[a[0]][a[1]] != 0:
            c = coloredMap[a[0]][a[1]]
        else:
            color += 1
        
        coloredMap[a[0]][a[1]] = c

        for d in [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]] :
            nxt = [a[0] + d[0], a[1] + d[1]]
            if nxt[0] < 0 or nxt[0] >= len(board) or nxt[1] < 0 or nxt[1] >= len(board):
                continue
            coloredMap[nxt[0]][nxt[1]] = c
            if not visited[nxt[0]][nxt[1]] and board[nxt[0]][nxt[1]] == 0:
                deq.append(nxt)
                visited[nxt[0]][nxt[1]] = True
        if len(deq) == 0:
            for i in range(1, len(zeros)):
                z = zeros[i]
                if not visited[z[0]][z[1]]:
                    deq.append(z)
                    visited[z[0]][z[1]] = True
                    break

test_case = int(input())

for t in range(1, test_case+1):
    N = int(input())
    m = []
    for i in range(N):
        m += [[c for c in input().rstrip()]]
    color = 1
    coloredMap = [[0 for _ in range(len(m))] for _ in range(len(m))]
    fillNumbers(m, coloredMap)
    count = color - 1
    for i in range(N) :
        for j in range(N) :
            if m[i][j] != "*" and coloredMap[i][j] == 0:
                count += 1
    print('#{} {}'.format(t, count))
