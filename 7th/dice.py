import copy
path = [    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 40, 0, 0, 0, 0, 0],
        2, 4, 6, 8, 
            [10, 13, 16, 19, 25, 30, 35, 40, 0, 0, 0, 0, 0], 
        12, 14, 16, 18, 
            [20, 22, 24, 25, 30, 35, 40, 0, 0, 0, 0, 0], 
        22, 24, 26, 28, 
            [30, 28, 27, 26, 25, 30, 35, 40, 0, 0, 0, 0, 0], 
        32, 34, 36, 38, 40, 0, 0, 0, 0, 0]

#path(0, 5, 10, 15), index, score
piece = [[0, 0, 0, []] for _ in range(4)]
dice = [int(i) for i in input().split(" ")]
limits = [len(path)-5, len(path[5])-5, len(path[10])-5, len(path[15])-5]
res = 0

def dfs(depth, piece, pieceIndex, diceIndex) :
    global dice, limits, res
    currentPiece = piece[pieceIndex]
    if(currentPiece[1] >= limits[currentPiece[0]//5]):
        return
    if(diceIndex >= len(dice)):
        s = 0
        for i in range(4):
            s += piece[i][2]
        if s == 213:
            print("----")
            for i in range(4):
                print(i, ":", piece[i][3], " sum = ", piece[i][2])
        res = max(res, s)
        return

    d = dice[diceIndex]
    
    tmp0 = copy.deepcopy(currentPiece[0])
    tmp1 = copy.deepcopy(currentPiece[1])

    currentPiece[1] += d
    if currentPiece[0] == 0:
        if currentPiece[1] == 5:
            currentPiece[0] = 5
            currentPiece[1] = 0
        elif currentPiece[1] == 10:
            currentPiece[0] = 10
            currentPiece[1] = 0
        elif currentPiece[1] == 15:
            currentPiece[0] = 15
            currentPiece[1] = 0

    for i in range(4):
        if i != pieceIndex:
            if path[piece[i][0]][piece[i][1]] == 0:
                continue 
            if path[piece[i][0]][piece[i][1]] == path[currentPiece[0]][currentPiece[1]]:
                currentPiece[0] = tmp0
                currentPiece[1] = tmp1
                return  
   
    currentPiece[2] += path[currentPiece[0]][currentPiece[1]]
    currentPiece[3] += [d]
    
    # for i in range(depth):
    #     print(" ",end='')
    # if currentPiece[0] == 0:
    #     print("[piece=",pieceIndex,"] ", "[dice=",d,"]", currentPiece[0], " : ", currentPiece[1], ": score of cur: ", currentPiece[2])
    # else:
    #     print("[piece=",pieceIndex,"] ", "[dice=",d,"]", currentPiece[0], " : ", currentPiece[1], ": score of cur: ", currentPiece[2])

    for i in range(4):
        dfs(depth+1, copy.deepcopy(piece), i, diceIndex+1)

dfs(0, piece, 0, 0)

print(res)