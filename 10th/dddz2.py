import pprint
import sys
import collections
import json

T = int(sys.stdin.readline())

m = [[0 for _ in range(T)] for _ in range(T)]
m2 = {}

for i in range(T-1) :
    line = list(map(int, sys.stdin.readline().split(" ")))
    m[line[0]-1][line[1]-1] = 1
    m[line[1]-1][line[0]-1] = 1
    if line[0]-1 in m2.keys():
        m2[line[0]-1] += [line[1]-1]
    else:
        m2[line[0]-1] = [line[1]-1]
    
    if line[1]-1 in m2.keys():
        m2[line[1]-1] += [line[0]-1]
    else:
        m2[line[1]-1] = [line[0]-1]

pprint.pprint(m2)

q = [0]
visited = []
history = [[] for _ in range(T)]
while q:
    print(q)
    a = q.pop()
    visited.append(a)
    for v in m2[a]:
        if v not in q+visited:
            q.append(v)


print(visited)

    

