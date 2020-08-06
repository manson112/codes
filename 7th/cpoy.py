import time

line = input().split(" ")
N = int(line[0])
L = int(line[1])
R = int(line[2])

A = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    l = input().split(" ")
    for j in range(len(l)):
        A[i][j] = int(l[j])

count = 0
while True:
    visited = [0] * (N*N)
    lastVisited = 0
    added = [0] * (N*N)
    added[0] = 1

    que = [[0, 0]]
    area = [0] * (N*N)
    sumOfPopulation = [0, 0]
    numOfUnited = [0, 0]
    anum = 1
    while sum(visited) != N*N :
        start4 = time.time()

        if(len(que) == 0) :
            for v in range(lastVisited, len(visited)):
                if visited[v] == 0:
                    que.append([v//N, v%N])
                    anum += 1
                    sumOfPopulation += [0]
                    numOfUnited += [0]
                    lastVisited = v+1
                    break
        print("start4 to end4 :", time.time()-start4)
        
        # print()
        # print(que)
        f = que.pop(0)
        cp = N*f[0]+f[1]
        if(visited[cp]) :
            continue
        # print(f)
        visited[cp] = 1
        area[cp] = anum
        sumOfPopulation[anum] += A[f[0]][f[1]]
        numOfUnited[anum] += 1
        # print(visited)

        start5 = time.time()
        cp2 = N*(f[0]-1) + f[1]
        if f[0]-1 >= 0 and L <= abs(A[f[0]-1][f[1]]-A[f[0]][f[1]]) <= R:
            if added[cp2] != 1:
                added[cp2] = 1
                que.append([f[0]-1, f[1]])
        cp3 = N*f[0] + f[1]-1
        if f[1]-1 >= 0 and L <= abs(A[f[0]][f[1]-1]-A[f[0]][f[1]]) <= R:
            if added[cp3] != 1:
                que.append([f[0], f[1]-1])
                added[cp3] = 1
        cp4 = N*(f[0]+1) + f[1]
        if f[0]+1 < N and L <= abs(A[f[0]+1][f[1]]-A[f[0]][f[1]]) <= R:
            if added[cp4] != 1:
                que.append([f[0]+1, f[1]])
                added[cp4] = 1
        cp5 = N*f[0] + f[1]+1
        if f[1]+1 < N and L <= abs(A[f[0]][f[1]+1]-A[f[0]][f[1]]) <= R:
            if added[cp5] != 1:
                que.append([f[0], f[1]+1])
                added[cp5] = 1
        print("start5 to end5 :", time.time()-start5)
        
        # print("After :", que)
    # print()
    # print(area)
    # print(sumOfPopulation)
    # print(numOfUnited)

    if anum == N*N:
        break

    for i in range(1, anum+1):
        population = sumOfPopulation[i]//numOfUnited[i]
        for j in range(len(area)):
            if area[j] == i :
                A[j//N][j%N] = population
    # print(A)
    
    count += 1

print(count)