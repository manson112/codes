

def solution(budgets, M):
    answer = 0
    if sum(budgets) <= M:
        return max(budgets)
    
    n = M // len(budgets)
    tmpM = M
    over = 0
    for b in budgets:
        if b <= n:
            tmpM -= b
        else:
            over += 1
    answer = tmpM // over


    return answer



print(solution([120, 110, 140, 150], 485))