import copy
N = 0
answer = False

def dfs(pa, totalVisited, currentVisited, const, cond, currentIndex) :
    global N, answer
    if len(totalVisited) == N:
        answer = True
        return
    
    totalVisited.add(currentIndex)
    currentVisited += [currentIndex]

    # if cond[]

    for node in pa[currentIndex]:
        if node not in const:
            dfs(pa, totalVisited.copy(), copy.deepcopy(currentVisited), const, cond, node)

def solution(n, path, order):
    global N
    N = n

    pa = [set() for _ in range(n)]
    for p in path:
        pa[p[0]].add(p[1])
        pa[p[1]].add(p[0])

    const = [k[1] for k in order]
    cond = [False for _ in range(n)]
    for k in order:
        cond[k] = True
    
    print(pa)

    dfs(pa, set(0), [0], order, const, cond, 0)
    return answer

print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]))