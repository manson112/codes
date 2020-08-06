import sys

line = sys.stdin.readline().split(" ")
N = int(line[0])
L = int(line[1])
R = int(line[2])

l = []
for i in range(N):
    l += sys.stdin.readline().split()
A = list(map(int, l))


count = 0
while True:
    visited = [0] * (N*N)
    added = [0] * (N*N)
    added[0] = 1

    que = [[0, 0]]
    area = [0] * (N*N)
    sumOfPopulation = [0, 0]
    numOfUnited = [0, 0]
    anum = 1
    while sum(visited) != N*N :

        if len(que) == 0 :
            for v in range(len(visited)-1, -1, -1):
                if visited[v] == 0:
                    que.append([v//N, v%N])
                    anum += 1
                    sumOfPopulation += [0]
                    numOfUnited += [0]
                    break
        
        f = que.pop(0)
        cp = N*f[0]+f[1]
        if(visited[cp]) :
            continue

        visited[cp] = 1
        area[cp] = anum
        sumOfPopulation[anum] += A[cp]
        numOfUnited[anum] += 1

        if f[0]-1 < 0 or f[1]-1 < 0 or f[0]+1 >= N or f[1]+1 >= N :
            continue

        cp2 = N*(f[0]-1) + f[1]
        if L <= abs(A[cp2]-A[cp]) <= R and added[cp2] != 1:
            added[cp2] = 1
            que.append([f[0]-1, f[1]])
        cp3 = N*f[0] + f[1]-1
        if L <= abs(A[cp3]-A[cp]) <= R and added[cp3] != 1:
            added[cp3] = 1
            que.append([f[0], f[1]-1])
        cp4 = N*(f[0]+1) + f[1]
        if L <= abs(A[cp4]-A[cp]) <= R and added[cp4] != 1:
            added[cp4] = 1
            que.append([f[0]+1, f[1]])
        cp5 = N*f[0] + f[1]+1
        if L <= abs(A[cp5]-A[cp]) <= R and added[cp5] != 1:
            added[cp5] = 1
            que.append([f[0], f[1]+1])

    if anum == N*N:
        break

    for i in range(1, anum+1):
        population = sumOfPopulation[i]//numOfUnited[i]
        for j in range(len(area)):
            if area[j] == i :
                A[j] = population
    count += 1

print(count)