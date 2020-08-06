import copy
import sys

def printCube(cube):
    print()
    print("          ----- ")
    for i in range(3):
        print("        | ", end='')
        for j in range(3):
            print(cube[2][i][j], end=' ')
        print("|")
    print("  -----   -----   -----   -----")
    for i in range(3):
        print("| ", end='')
        for j in [3, 0, 4, 5]:
            for k in range(3):
                print(cube[j][i][k], end=' ')
            print("| ", end='')
        print()
    print("  -----   -----   -----   -----")
    for i in range(3):
        print("        | ", end='')
        for j in range(3):
            print(cube[1][i][j], end=' ')
        print("|")
    print("          ----- ")
    print()
    

def makeCube():
    cube = [
        [["w", "w", "w"] for _ in range(3)],
        [["r", "r", "r"] for _ in range(3)],
        [["o", "o", "o"] for _ in range(3)],
        [["g", "g", "g"] for _ in range(3)],
        [["b", "b", "b"] for _ in range(3)],
        [["y", "y", "y"] for _ in range(3)]
    ]
    return cube

    
def rotateU(cube, k) :
    for i in range(k):
        tmp = copy.deepcopy(cube[0][0])
        cube[0][0][0] = cube[0][2][0]
        cube[0][0][1] = cube[0][1][0]
        cube[0][0][2] = tmp[0]
        cube[0][1][0] = cube[0][2][1]
        cube[0][2][0] = cube[0][2][2]
        cube[0][2][1] = cube[0][1][2]
        cube[0][2][2] = tmp[2]
        cube[0][1][2] = tmp[1]

        tmp = copy.deepcopy(cube[1][0])
        cube[1][0][0] = cube[4][2][0]
        cube[1][0][1] = cube[4][1][0]
        cube[1][0][2] = cube[4][0][0]

        cube[4][2][0] = cube[2][2][2]
        cube[4][1][0] = cube[2][2][1]
        cube[4][0][0] = cube[2][2][0]

        cube[2][2][0] = cube[3][2][2]
        cube[2][2][1] = cube[3][1][2]
        cube[2][2][2] = cube[3][0][2]

        cube[3][0][2] = tmp[0]
        cube[3][1][2] = tmp[1]
        cube[3][2][2] = tmp[2]

        print("============Rotate[",(i+1),"]============")
        printCube(cube)
        print("=========================================")


def turnRight(cube, k) :
    for i in range(k):
        tmp = copy.deepcopy(cube[0])
        cube[0] = copy.deepcopy(cube[3])
        cube[3] = copy.deepcopy(cube[5])
        cube[5] = copy.deepcopy(cube[4])
        cube[4] = copy.deepcopy(tmp)
        
        tmp = copy.deepcopy(cube[2][0])
        cube[2][0][0] = tmp[2]
        cube[2][0][1] = cube[2][1][2]
        cube[2][0][2] = cube[2][2][2]
        cube[2][1][2] = cube[2][2][1]
        cube[2][2][2] = cube[2][2][0]
        cube[2][2][1] = cube[2][1][0]
        cube[2][2][0] = tmp[0]
        cube[2][1][0] = tmp[1]

        tmp = copy.deepcopy(cube[1][0])
        cube[1][0][0] = cube[1][2][0]
        cube[1][0][1] = cube[1][1][0]
        cube[1][0][2] = tmp[0]

        cube[1][1][0] = cube[1][2][1]
        cube[1][2][0] = cube[1][2][2]

        cube[1][2][0] = cube[1][2][2]
        cube[1][2][1] = cube[1][1][2]
        cube[1][2][2] = tmp[2]

        cube[1][1][2] = tmp[1]

        

def turnUp(cube, k) :
    for i in range(k):
        tmp = copy.deepcopy(cube[0])
        cube[0] = copy.deepcopy(cube[1])

        cube[1][0][0] = cube[5][2][2]
        cube[1][0][1] = cube[5][2][1]
        cube[1][0][2] = cube[5][2][0]
        cube[1][1][0] = cube[5][1][2]
        cube[1][1][1] = cube[5][1][1]
        cube[1][1][2] = cube[5][1][0]
        cube[1][2][0] = cube[5][0][2]
        cube[1][2][1] = cube[5][0][1]
        cube[1][2][2] = cube[5][0][0]

        cube[5][0][0] = cube[2][2][2]
        cube[5][0][1] = cube[2][2][1]
        cube[5][0][2] = cube[2][2][0]
        cube[5][1][0] = cube[2][1][2]
        cube[5][1][1] = cube[2][1][1]
        cube[5][1][2] = cube[2][1][0]
        cube[5][2][0] = cube[2][0][2]
        cube[5][2][1] = cube[2][0][1]
        cube[5][2][2] = cube[2][0][0]

        cube[2] = copy.deepcopy(tmp)
        
        tmp = copy.deepcopy(cube[3][0])
        cube[3][0][0] = tmp[2]
        cube[3][0][1] = cube[3][1][2]
        cube[3][0][2] = cube[3][2][2]
        cube[3][1][2] = cube[3][2][1]
        cube[3][2][2] = cube[3][2][0]
        cube[3][2][1] = cube[3][1][0]
        cube[3][2][0] = tmp[0]
        cube[3][1][0] = tmp[1]

        tmp = copy.deepcopy(cube[4][0])
        cube[4][0][0] = cube[4][2][0]
        cube[4][0][1] = cube[4][1][0]
        cube[4][0][2] = tmp[0]
        cube[4][1][0] = cube[4][2][1]
        cube[4][2][0] = cube[4][2][2]
        cube[4][2][1] = cube[4][1][2]
        cube[4][2][2] = tmp[2]
        cube[4][1][2] = tmp[1]
        print("============Turn Up[",(i+1),"]============")
        printCube(cube)
        print("=========================================")
        print()


test_case = int(sys.stdin.readline().rstrip())

for i in range(test_case):
    n = int(sys.stdin.readline().rstrip())
    cmd = str(sys.stdin.readline().rstrip()).split(" ")
    cube = makeCube()
    for j in range(n):
        k = 1
        if cmd[j][1] == "-" :
            k = 3
        if cmd[j][0] == "U":
            rotateU(cube, k)
        elif cmd[j][0] == "R":
            turnRight(cube, 3)
            rotateU(cube, k)
            turnRight(cube, 1)
        elif cmd[j][0] == "L":
            turnRight(cube, 1)
            rotateU(cube, k)
            turnRight(cube, 3)
        elif cmd[j][0] == "F":
            turnUp(cube, 1)
            rotateU(cube, k)
            turnUp(cube, 3)
        elif cmd[j][0] == "B":
            turnUp(cube, 3)
            rotateU(cube, k)
            turnUp(cube, 1)
        elif cmd[j][0] == "D":
            turnUp(cube, 2)
            rotateU(cube, k)
            turnUp(cube, 2)
        # printCube(cube)
    for i in range(3):
        for j in range(3):
            print(cube[0][i][j], end='')
        print()




