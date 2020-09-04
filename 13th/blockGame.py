import pprint
import collections

shapes =[[[0,0],[1,0],[1,1],[1,2]], 
        [[0,1],[1,1],[2,0],[2,1]], 
        [[0,0],[1,0],[2,0],[2,1]], 
        [[0,2],[1,0],[1,1],[1,2]],
        [[0,1],[1,0],[1,1],[1,2]]]

needToFill = [[[0,1],[0,2]], [[0,0],[1,0]],
                [[0,1],[1,1]], [[0,0],[0,1]], [[0,0],[0,2]]]
def removeBlock(board, block) :
    for i in range(4):
        board[block[i][0]][block[i][1]] = 0

def find(board, i, j, num) :
    global shapes, needToFill
    l = []
    deq = collections.deque()
    deq.append([i, j])
    visited = [[i, j]]
    count = 1
    minX, minY = i, j
    
    # BFS
    while deq :
        a = deq.popleft()
        l += [a]
        for d in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            nxt = [a[0]+d[0], a[1]+d[1]]
            if 0 <= nxt[0] < len(board) and 0 <= nxt[1] < len(board):
                if board[nxt[0]][nxt[1]] == num and nxt not in visited:
                    deq.append(nxt)
                    visited.append(nxt)
                    count += 1 
                    if nxt[0] < minX: minX = nxt[0]
                    if nxt[1] < minY: minY = nxt[1]
        if count == 4:
            break
    l.extend(deq)

    # 모양 찾기
    shape = []
    for i in range(4):
        shape += [[l[i][0]-minX, l[i][1]-minY]]
    shape = sorted(shape, key=lambda x: (x[0], x[1]))
    shapeIndex = 0
    try :
        shapeIndex = shapes.index(shape)
    except:
        shapeIndex = -1
    
    # 채워야 하는 칸
    need = []
    if shapeIndex != -1:
        for i in range(2):
            need += [[needToFill[shapeIndex][i][0]+minX, needToFill[shapeIndex][i][1] + minY]]
    return shapeIndex, need, l
    

def solution(board):
    answer = 0
    # BFS 이용 : 0이 아닌 숫자를 만나면 BFS로 모양을 찾고 분류
    # 이미 나온 숫자는 다시 나올 수 없으므로 visited에 저장
    visited = {}
    checkList = {}
    for i in range(len(board)) :
        for j in range(len(board)):
            if board[i][j] != 0 and board[i][j] not in visited.keys():
                shapeIndex, need, block = find(board, i, j, board[i][j])
                if shapeIndex != -1:
                    checkList[board[i][j]] = [shapeIndex, need, block]
                visited[board[i][j]] = True
    checkCount = 0
    totalCount = len(checkList)
    while checkCount < totalCount:
        newCheckList = {}
        for k, v in checkList.items():
            s = v[0]
            need = v[1]
            allClear = True
            for i in range(len(need)):
                needPass = False
                for j in range(need[i][0], -1, -1):
                    if board[j][need[i][1]] != 0:
                        allClear = False
                        if board[j][need[i][1]] in checkList.keys():
                            newCheckList[k] = v
                            break
                        else:
                            checkCount+=1
                            break
                if not allClear :
                    break
            if allClear :
                checkCount+=1
                answer += 1
                removeBlock(board, v[2])
        checkList = newCheckList

    return answer


print(solution([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]))