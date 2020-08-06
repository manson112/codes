
class Robot :
    dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    loc = [[0,1], [0,0]]
    direction = 0

    board = []

    def __init__(self, board) :
        self.board = board

    def move(self):
        print("before : ", self.loc)
        next = [self.loc[0][0] + self.dir[self.direction][0], self.loc[0][1] + self.dir[self.direction][1]]
        if self.board[next[0]][next[1]] == 0 and next[0] >= 0 and next[0] < len(self.board) and next[1] >= 0 and next[1] < len(self.board):
            self.loc = [next] + self.loc
            self.loc.pop()
        else :
            self.rotate()
        print("after : ", self.loc)
    def check(self):
        if self.loc[0] == [len(self.board), len(self.board)] or self.loc[1] == [len(self.board), len(self.board)] :
            return True
        return False
    
    def rotate(self):
        if self.direction == 0:
            if self.board[loc[1][loc[1][0]+1]
        self.direction = (self.direction+1)%4

def solution(board):
    answer = 0
    
    r = Robot(board)
    r.move()
    
    return answer


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))