import sys
import pprint

def cmp(a, b):
    if a[1] > b[1]:
        return -1
    elif a[1] < b[1]:
        return 1
    return 0

N, C = map(int, sys.stdin.readline().split(" "))
M = int(sys.stdin.readline())

m = []

for i in range(M):
    (a, b, c) = map(int, sys.stdin.readline().split(" "))
    m += [c]

sorted(m, key= lambda s: s[1])
print(m)