import sys
import pprint
from itertools import permutations
import json

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def rotate(start, end, m):
    if start == end:
        return
    s = (start[0], end[1])
    cur = (start[0], end[1])
    sd = 0
    d = 0
    while True:
        cur = (cur[0]+dx[d], cur[1]+dy[d])
        m[cur[0]][cur[1]], m[s[0]][s[1]] = m[s[0]][s[1]], m[cur[0]][cur[1]]
        s = (s[0]+dx[sd], s[1]+dy[sd])
        if s == start or s == end or s == (end[0], start[1]):
            sd = (sd+1) % 4
        if cur == start or cur == end or cur == (end[0], start[1]):
            d = (d+1) % 4
        if cur == (start[0]+1, end[1]) :
            break

    rotate((start[0]+1, start[1]+1), (end[0]-1, end[1]-1), m)    
    
(N, M, K) = map(int, sys.stdin.readline().split(" "))

m = []
minimum = 100000
ops = []
for i in range(N):
    m += [list(map(int, sys.stdin.readline().split(" ")))]

for i in range(K):
    (r, c, s) = map(int, sys.stdin.readline().split(" "))
    ops += [(r, c, s)]

perm = permutations([i for i in range(K)])
for p in list(perm):
    tmp = json.loads(json.dumps(m))
    for i in p:
        op = ops[i]
        (r, c, s) = (op[0], op[1], op[2])
        start = (r-s-1, c-s-1)
        end = (r+s-1, c+s-1)
        rotate(start, end, tmp)
    for j in range(N):
        minimum = min(minimum, sum(tmp[j]))

print(minimum)