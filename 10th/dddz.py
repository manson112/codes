import pprint
import sys
import collections
import json

T = int(sys.stdin.readline())

m = [[0 for _ in range(T)] for _ in range(T)]
m2 = [[] for _ in range(T)]

for i in range(T-1) :
    line = list(map(int, sys.stdin.readline().split(" ")))
    m[line[0]-1][line[1]-1] = 1
    m[line[1]-1][line[0]-1] = 1
    m2[line[0]-1] += [line[1]-1]
    m2[line[1]-1] += [line[0]-1]

pprint.pprint(m2)

visited = [False for _ in range(T)]

s = set()

q = collections.deque()
q.append((0, [0], [False for _ in range(T)]))
isFirst = True
while q:
    a = q.popleft()
    if a[2][a[0]]:
        continue
    a[2][a[0]] = True
    connected = m2[a[0]]
    print(a)
    flg = False
    if len(connected) == 1 and len(a[1]) < 4 and not isFirst:
        flg = True
    if isFirst:
        isFirst= False

    if len(a[1]) == 4:
        s.add(frozenset(a[1]))
        a[1].pop(0)

    for c in connected:
        visited = json.loads(json.dumps(a[2]))
        if flg:
            visited[c] = False
            newA = a[1][:-2] + [a[1][-1]] + [a[1][-2]]
            q.append((c, newA, visited))
        else:
            q.append((c, a[1] + [c], visited))

    
print(s)