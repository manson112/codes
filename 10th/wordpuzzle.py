
def solution(strs, t):
    answer = 0
    maximum = len(t)
    result = [maximum+1 for _ in range(10)]
    print(result)
    for i in range(maximum):
        for j in range(len(strs)):
            p = len(strs[j])-1
            q = 0
            for q in range(len(strs[j])):
                print(p, q)
                if (p-q < 0 or i-q<0) and str[j][p-q] == t[i-q]:
                    continue
                else:
                    break
            if q == len(strs[j]):
                if i-q >= 0:
                    result[i] = min(result[i], 1+ result[i-q])
                else:
                    result[i] = 1
    return answer


print(solution(["ba","na","n","a"], "banana"))