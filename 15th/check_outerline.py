def solution(n, weak, dist):
    answer = 0
    people = 0

    dist.sort()
    print(weak)
    totalWeakDistance = 0

    isolated = [False for _ in range(len(weak))]
    d = []
    for i in range(1, len(weak)):
        if weak[i] - weak[i-1] > 100 or weak[i] - weak[i-1] > dist[-1]:
            people += 1
            if isolated[i-1] :
                totalWeakDistance += 1
            isolated[i-1] = True
            isolated[i] = True
        else:
            d += [[(weak[i-1], weak[i]), weak[i]-weak[i-1]]]
    if n + weak[0] - weak[-1] <= 100 and n + weak[0] - weak[-1] <= dist[-1]:
        d += [[(weak[len(weak)-1], weak[0]), n + weak[0] - weak[-1]]]
    else:
        people += 1
        if isolated[-1]:
            totalWeakDistance += 1
            if isolated[0]:
                totalWeakDistance += 1

    if people > len(dist):
        return -1
        
    d = sorted(d, key=lambda x: x[1])
    print(d)
    print("people:", people)
    
    for i in range(len(d)):
        totalWeakDistance += d[i][1]
    
    print("total Need:", totalWeakDistance)

    tmp = totalWeakDistance
    print(d)
    print(dist)
    while people <= len(dist):
        print("total distance remained:", tmp)
        selected = dist[-people:]
        print("selected:",selected)
        sumOfSelected = sum(selected)
        print("sum of selected:",sumOfSelected)
        if sumOfSelected >= tmp:
            break
        tmp -= d[-1][1]
        d.pop()    
        people += 1

    if people > len(dist):
        return -1

    return people


print(solution(200, [0, 100], [1, 1]))