from functools import cmp_to_key
def customSort(x, y):
    if x[1] > y[1]:
        return -1
    elif x[1] == y[1]:
        if x[0] < y[0]:
            return -1
        else:
            return 1
    return 1

def solution(N, stages):
    answer = []

    count = 0
    dic = {}
    for s in stages:
        if s in dic.keys():
            dic[s] += 1
        else:
            dic[s] = 1 

    rates = {}
    s = 0

    for i in range(N+1, 0, -1):
        try:
            s += dic[i]
            rate = dic[i] / s
            rates[i] = rate
        except:
            rates[i] = 0
    rates.pop(N+1)
    answer = [item[0] for item in sorted(rates.items(), key=cmp_to_key(customSort))]

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))