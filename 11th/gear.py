import sys
import pprint

# 문자열 회전 
def rotate(gear, i):
    # 시계방향
    if i == 1:
        g = str(gear[-1]) + str(gear[:-1])
    # 반시계 방향
    else:
        g = str(gear[1:]) + str(gear[0])
    return g

gears = []
for i in range(4):
    gears += [sys.stdin.readline().rstrip()]

K = int(sys.stdin.readline())
L = []
for i in range(K):
    (A, B) =(map(int, sys.stdin.readline().split(" ")))
    L += [(A-1, B)]

for i in range(K):
    (A, B) = L[i]
    rotations = []

    # 좌측 회전 톱니 저장
    tmp = A
    tmpB = B
    for j in range(A-1, -1, -1):
        if gears[tmp][6] != gears[j][2]:
            rotations += [(j, -1*tmpB)]
        else:
            break
        tmp = j
        tmpB *= -1

    # 우측 회전 톱니 저장
    tmp = A
    tmpB = B
    for j in range(A+1, 4):
        if gears[tmp][2] != gears[j][6]:
            rotations += [(j, -1*tmpB)]
        else:
            break
        tmp = j
        tmpB *= -1

    # 자신 회전
    gears[A] = rotate(gears[A], B)

    # 나머지 톱니 회전
    for j in range(len(rotations)):
        r = rotations[j]
        gears[r[0]] = rotate(gears[r[0]], r[1])

s = 0
c = 1
for i in range(4):
    s += int(gears[i][0]) * c
    c *= 2

print(s)