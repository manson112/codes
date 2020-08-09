import sys
import pprint

class Robot:
    # E, S, W, N
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    def __init__(self, num, x, y, d):
        super().__init__()
        self.num = num
        self.x = x
        self.y = y
        self.direction = d
    def changeDir(self, d):
        if d == "L":
            self.direction = (self.direction+3)%4
        elif d == "R":
            self.direction = (self.direction+1)%4
    def nxt(self):
        return self.x+self.dx[self.direction], self.y+self.dy[self.direction]
    def move(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return str(self.num)
    def __repr__(self):
        return str(self)
    

def changePoint(B, x, y):
    return B-y, x-1

def convertDir(d):
    if d == "E":
        return 0
    elif d == "S":
        return 1
    elif d == "W":
        return 2
    elif d == "N": 
        return 3

(A, B) = (map(int, sys.stdin.readline().split(" ")))
(N, M) = (map(int, sys.stdin.readline().split(" ")))

m = [[0 for _ in range(A)] for _ in range(B)]
robots = {}

for i in range(N):
    x, y, d = (map(str, sys.stdin.readline().rstrip().split(" ")))
    x, y = changePoint(B, int(x), int(y))
    r = Robot(i+1, x, y, convertDir(d))
    robots[i+1] = r
    m[x][y] = r


crashIntoWall = False
crashIntoRobot = False

operations = []
for i in range(M):
    (n, o, c) = (map(str, sys.stdin.readline().rstrip().split(" ")))
    operations += [(n, o, c)]

res = "OK"
for i in range(M):
    (n, o, c) = operations[i]
    n = int(n)
    c = int(c)
    r = robots[n]
    if o == "F":
        tmpX, tmpY = r.x, r.y
        for count in range(c):
            nxtX, nxtY = r.nxt()
            if nxtX < 0 or nxtX >= B or nxtY < 0 or nxtY >= A:
                crashIntoWall = True
                res = "Robot " + str(n) + " crashes into the wall"
                break
            if m[nxtX][nxtY] != 0:
                crashIntoRobot = True
                res = "Robot " + str(n) + " crashes into robot " + str(m[nxtX][nxtY].num)
                break
            r.move(nxtX, nxtY)
           
        if crashIntoRobot or crashIntoWall:
            break
        m[tmpX][tmpY] = 0
        m[r.x][r.y] = r
    else:
        for j in range(c%4):
            r.changeDir(o)

print(res)