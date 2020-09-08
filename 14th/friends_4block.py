def check(board, checkBoard):
    count = 0
    removeList = []
    for i in range(len(board)-1):
        for j in range(len(board[0])-1):
            if board[i][j] == '':
                continue
            cur = board[i][j]
            allSame = True
            for d in [[1, 0], [0, 1], [1, 1]]:
                if cur != board[i+d[0]][j+d[1]]:
                    allSame = False
                    break
            if allSame:
                for d in [[0, 0], [1, 0], [0, 1], [1, 1]]:
                    if not checkBoard[i+d[0]][j+d[1]]:
                        count += 1 
                        removeList.append([i+d[0], j+d[1]])
                    checkBoard[i+d[0]][j+d[1]] = True
    return count, removeList
            

def solution(m, n, b):
    answer = 0

    board = []
    for j in range(len(b[0])):
        l = []
        for i in range(len(b)-1, -1, -1):
            l += [b[i][j]]
        board += [l]
    checkBoard = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

    while True:
        checkBoard = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        c, rmList = check(board, checkBoard)
        if c == 0:
            break
        rmList = sorted(rmList, key=lambda x: x[1])
        for r in range(len(rmList)-1, -1, -1):
            board[rmList[r][0]].pop(rmList[r][1])
            board[rmList[r][0]].append('')
        
        answer += c
    return answer

print(solution(4,5, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))