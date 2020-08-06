def solution(gems):
    answer = []
    flg = True
    gem = set(gems)
    dp = [[] for _ in range(len(gems)+1)]

    allTrue = False 
    index = 0
    while not allTrue:
        if index >= len(gems) or index+len(gem) > len(gems):
            break
        tmpGem = set()
        for j in range(index, index + len(gem)):
            tmpGem.add(gems[j])
        if len(tmpGem) == len(gem) :
            answer += [1]
            answer += [len(gem)]
            flg = False
            break
        dp[len(gem)] += [tmpGem]
        index += 1
    if flg :
        for size in range(len(gem)+1, len(gems)+1):
            allTrue = False
            index = 0
            while not allTrue:
                if index >= len(gems) or index+size > len(gems) :
                    break
                tmpGem = dp[size-1][index].copy()
                tmpGem.add(gems[index+size-1])
                if len(tmpGem) == len(gem):
                    answer += [index+1]
                    answer += [index+size]
                    allTrue = True
                    break
                dp[size] += [tmpGem]
                index += 1
            if allTrue:
                break

    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))