def solution(gems):
    answer = []
    gem = set(gems)
    gemMap = {}
    tmpSet = set()

    length = 9999999
    h = 1
    l = 1
    foundedHigh = 0

    for low in range(len(gems)):
        foundHigh = False
        for high in range(foundedHigh, len(gems)):
            if gems[high] not in gemMap.keys():
                gemMap[gems[high]] = 1
                tmpSet.add(gems[high])
            else :
                gemMap[gems[high]] += 1
            if len(tmpSet) == len(gem) :
                if abs(high-low) < length:
                    l = low
                    h = high
                    length = abs(high-low)
                foundedHigh = high
                foundHigh = True
                break

        if not foundHigh :
            break

        if gems[foundedHigh] in gemMap.keys():
            if gemMap[gems[foundedHigh]] == 1:
                del gemMap[gems[foundedHigh]]
                tmpSet.remove(gems[foundedHigh])
            else :
                gemMap[gems[foundedHigh]] -= 1
        if gems[low] in gemMap.keys() :
            if gemMap[gems[low]] == 1:
                del gemMap[gems[low]]
                tmpSet.remove(gems[low])
            else:
                gemMap[gems[low]] -= 1
            
    answer += [l+1, h+1]
    return answer




print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))