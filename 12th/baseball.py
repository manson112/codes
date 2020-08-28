import sys
from itertools import permutations

current = -1
class Board:
    def __init__(self):
        super().__init__()
        self.board = [0, 0, 0]
    def run(self, c) :
        if c == 1:
            s = self.board[2]
            self.board = [1] + self.board[:2]
            return s
        elif c == 2:
            s = sum(self.board[1:])
            self.board = [0, 1] + [self.board[0]]
            return s
        elif c == 3:
            s = sum(self.board)
            self.board = [0, 0, 1]
            return s
        elif c == 4:
            s = sum(self.board) + 1
            self.board = [0, 0, 0]
            return s
    def reset(self):
        self.board = [0, 0, 0]

def nxt():
    global current
    current = (current+1)%9

N = int(sys.stdin.readline())

scores = []
for i in range(N) :
    l = list(map(int, sys.stdin.readline().split(" ")))
    scores += [l]

perm = permutations([2,3,4,5,6,7,8,9])
maxScore = 0
for p in list(perm):
    order = list(p[:3]) + [1] + list(p[3:])
    currentInning = 0
    outCount = 3
    score = 0
    board = Board() 
    current = -1
    while currentInning < N:
        nxt()
        b = scores[currentInning][order[current]-1]
        if b == 0:
            outCount -= 1
        else :
            score += board.run(b)

        if outCount == 0:
            currentInning += 1
            outCount = 3
            board.reset()

    maxScore = max(maxScore, score)
print(maxScore)

