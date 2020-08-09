import sys
import pprint

class Space:
    
    def __init__(self, piece, color):
        super().__init__()
        self.pieces = []
        # 0 = white, 1 = red, 2 = blue
        self.color = color
        # list에 칸에 존재하는 말 저장
        if piece != None:
            self.pieces += [piece]

    def add(self,piece):
        reversedList = [piece]
        if self.color == 1:
            # 빨간 색일 때, 새로운 피드들의 순서만 변경
            tmp = piece.over
            while tmp:
                reversedList = [tmp] + reversedList
                tmp = tmp.over
            for p in reversedList:
                p.over, p.under = p.under, p.over
        else:
            p = piece.over
            while p:
                reversedList += [p]
                p = p.over
        
        # 기존 말의 위에 새로운 말 링크
        if len(self.pieces) != 0:
            self.pieces[-1].over = reversedList[0]
            reversedList[0].under = self.pieces[-1]

        self.pieces += reversedList

        
        
    def remove(self, piece):
        # print("----BEFORE----")
        # print(self.pieces)
        index = self.pieces.index(piece)
        if index != 0:
            self.pieces[index-1].over = None
            piece.under = None
        del self.pieces[index:]
        # print("----AFTER----")
        # print(self.pieces)
        # print()

    def __str__(self):
        if len(self.pieces) == 0:
            return str(self.color)
        else:
            s = "{"
            for i in range(len(self.pieces)):
                s += str(self.pieces[i])
                if i != len(self.pieces)-1:
                    s += ","
            s += "}"
            return s
    def __repr__(self):
        return str(self)
        
class Piece:
    # E, W, N, S
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    def __init__(self, num, x, y, d):
        super().__init__()
        self.num = num
        self.x = x
        self.y = y
        self.direction = d
        self.under = None
        self.over = None

    # 다음 좌표
    def nxt(self):
        return self.x + self.dx[self.direction], self.y + self.dy[self.direction]

    # 방향 전환
    def changeDir(self):
        if self.direction == 0 or self.direction == 1:
            self.direction = 1 - self.direction
        else:
            self.direction = 5 - self.direction

    def move(self, x ,y):
        self.x = x
        self.y = y

        # 움직일 때 위에 있는 보든 말들의 좌표도 이동
        tmp = self.over
        while tmp:
            tmp.x = x
            tmp.y = y
            tmp = tmp.over
        # print("PIECE[", self.num, "]\'s location is changed to (", self.x, ",", self.y,")" )
        # print()
    def __str__(self):
        return str(self.num)
    def __repr__(self):
        return str(self)
        

(N, K) = (map(int, sys.stdin.readline().split(" ")))

m = []
for i in range(N):
    line = list(map(int, sys.stdin.readline().split(" ")))
    l = []
    for j in range(len(line)):
        l += [Space(None, line[j])]
    m += [l]

dic = {}
for i in range(K):
    (x, y, d) = (map(int, sys.stdin.readline().split(" ")))
    p = Piece(i, x-1, y-1, d-1)
    dic[i] = p
    m[x-1][y-1] = Space(p, m[x-1][y-1].color)

t = 0
founded = False
while t < 1001:
    for i in range(K):
        piece = dic[i]
        # print(f'[{piece.num}] : dir = {piece.direction}, (x={piece.x}, y={piece.y})')
        
        # 다음 좌표
        nxtX, nxtY = piece.nxt()
        # print(f'nxt = ({nxtX},{nxtY})')

        # 벽 or 파란색
        if nxtX < 0 or nxtX >= N or nxtY < 0 or nxtY >= N or m[nxtX][nxtY].color == 2:
            piece.changeDir()

        # 다음 좌표
        nxtX, nxtY = piece.nxt()
        # print(nxtX, nxtY)

        # 방향 전환 후 벽이거나 파란색
        if nxtX < 0 or nxtX >= N or nxtY < 0 or nxtY >= N or m[nxtX][nxtY].color == 2:
            continue

        # 보드에서 지움
        m[piece.x][piece.y].remove(piece)
        # 움직임
        piece.move(nxtX, nxtY)
        # 보드에 추가
        m[nxtX][nxtY].add(piece)

        # pprint.pprint(m)
        if len(m[nxtX][nxtY].pieces) >= 4:
            founded = True
            break
    t+= 1
    if founded:
        break

if t > 1000:
    print(-1)
else:
    print(t)