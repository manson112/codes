import sys
import pprint
import json
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 상어 : 번호, 위치, 방향, 우선순위
class Shark:
    def __init__(self, num, loc):
        super().__init__()
        self.num = num
        self.loc = loc
        self.direction = 0
        self.priority = []

    def getCurrentPrioriy(self):
        return self.priority[self.direction-1]

    def __str__(self):
        return str(self.loc)+ " " + str(self.direction)
    def __repr__(self):
        return str(self)

# Space: 현재 상어(없으면 None), 냄새, 냄새 지속 시간
class Space:
    def __init__(self, shark, k):
        super().__init__()
        if shark != None:
            self.current = shark
            self.smell = shark.num
            self.k = k 
        else:
            self.current = None
            self.smell = 0
            self.k = 0

    # 냄새 감소
    def decreaseSmell(self):
        if self.k == 0:
            return
        if self.current == None:
            self.k -= 1
        if self.k == 0:
            self.smell = 0

    def __str__(self):
        return "(" + str(self.smell) + ", " + str(self.k) +")"

    def __repr__(self):
        return str(self)

firstLine = list(map(int, sys.stdin.readline().split()))

N, M, K = firstLine[0], firstLine[1], firstLine[2]

# 상어들의 pointer 저장
sharkLoc = {}

# map을 Space객체로 채움(None => 상어 없음)
mmap = []
for i in range(N):
    l = []
    line = list(map(int, sys.stdin.readline().split()))
    for ind in range(len(line)):
        if line[ind] == 0:
            l += [Space(None, K)]
        else:
            newShark = Shark(line[ind], (i, ind))
            l += [Space(newShark, K)]
            #상어 저장
            sharkLoc[line[ind]] = newShark
    mmap += [l]

initDir = list(map(int, sys.stdin.readline().split()))

# 상어 초기 방향 설정
for k, v in sharkLoc.items():
    v.direction = initDir[k-1]

# 상어 우선순위 저장
for i in range(M * 4):
    pri = list(map(int, sys.stdin.readline().split()))
    sharkLoc[i//4 + 1].priority += [pri]

t = 0
while t < 1000:
    # 겹치는 상황 감지하기 위한 빈 맵과 딕셔너리
    newMap = [[Space(None, K) for _ in range(N)] for _ in range(N)]
    newDict = {}

    # 존재하는 상어들에 한해서 반복
    for k, v in sharkLoc.items():
        # True: 주위에 빈 공간이 있음
        flg = False
        foundedX = 0
        foundedY = 0
        foundedDir = 0
        for d in v.getCurrentPrioriy():
            nxtX = v.loc[0] + dx[d-1] 
            nxtY = v.loc[1] + dy[d-1]
            if nxtX < 0 or nxtX >= N or nxtY < 0 or nxtY >= N:
                continue

            # 빈 칸이 아닐 때
            if mmap[nxtX][nxtY].smell != 0:
                # 자신의 냄새 일 경우 가장 처음 나온 자신의 방향 저장
                if mmap[nxtX][nxtY].smell == v.num and foundedDir == 0:
                    foundedDir = d
                # 빈칸이 있는지 계속 확인
                continue

            # 빈 칸이 있을 때
            flg = True
            foundedX = nxtX
            foundedY = nxtY
            foundedDir = d
            break

        # 빈칸은 못 찾았을 때 우선순위가 높은 자신의 방향으로 이동 
        if not flg and foundedDir != 0 :
            foundedX = v.loc[0] + dx[foundedDir-1]
            foundedY = v.loc[1] + dy[foundedDir-1]

        # 이동한 위치에 상어가 있는 경우
        if newMap[foundedX][foundedY].current != None :
            # 자신보다 번호가 크다면 대체
            if newMap[foundedX][foundedY].current.num > v.num:
                # 현재 위치에서 자신을 삭제
                mmap[v.loc[0]][v.loc[1]].current = None
                # 방향과 위치 변경
                v.direction = foundedDir
                v.loc = (foundedX, foundedY)

                # 이전에 존재하던 상어를 newDict 에서 제거
                if newMap[foundedX][foundedY].current.num in newDict.keys() :
                    newDict.pop(newMap[foundedX][foundedY].current.num)
                
                # 자신을 새 위치로 이동 
                newMap[foundedX][foundedY] = Space(v, K)

                # newDict에 추가
                newDict[v.num] = v
            # 자신이 번호가 크면 삭제
            else:
                mmap[v.loc[0]][v.loc[1]].current = None
        # 그냥 이동
        else:
            mmap[v.loc[0]][v.loc[1]].current = None
            v.direction = foundedDir
            v.loc = (foundedX, foundedY)
            newMap[foundedX][foundedY] = Space(v, K)
            newDict[v.num] = v

    # 새로운 위치를 기존 지도에 추가
    for k, v in newDict.items():
        mmap[v.loc[0]][v.loc[1]] = Space(v, K)
    
    # 새로 이동한 위치를 제외한 나머지 냄새 감소
    for i in range(N):
        for j in range(N):
            mmap[i][j].decreaseSmell()

    # 남은 상어 update
    sharkLoc = newDict

    if len(sharkLoc) == 1:
        break

    t += 1
if t >= 1000:
    print(-1)
else:
    print(t+1)