import json
allList = []

def getList(l, keys, current, size):
    global allList
    if current > len(keys):
        return
    if len(l) == size:
        allList += [l]
        return
    tmp = json.loads(json.dumps(l))
    for i in range(current, len(keys)):
        getList(tmp + [keys[i]], keys, i+1, size)

def dfs(keys, current, size):
    for i in range(len(keys)):
        getList([keys[i]], keys, i+1, size)

def solution(relation):
    global allList
    answer = 0
    N, M = len(relation), len(relation[0])
    candidate = []
    duplicates = {}
    for j in range(M):
        dic = {}
        isCandidateKey = True
        duplicateSet = set()
        for i in range(N):
            if relation[i][j] in dic.keys():
                dic[relation[i][j]] += [i]
                duplicateSet.add(relation[i][j])
                isCandidateKey = False
            else :
                dic[relation[i][j]] = [i]
        for s in duplicateSet:
            if j in duplicates.keys():
                duplicates[j] += dic[s]
            else:
                duplicates[j] = dic[s]
        if isCandidateKey:
            candidate += [j]
    keys = list(duplicates.keys())
    for i in range(2, len(keys)+1):
        getList([], keys, 0, i)
        # print(allList)
        for al in allList:
            checkAlready = False
            # print("======", al)
            for i in range(len(candidate)):
                # print("--", candidate[i])
                try :
                    checkAlready = all(item in al for item in candidate[i])
                except :
                    checkAlready = candidate[i] in al
                if checkAlready:
                    break
            if checkAlready :
                continue
            t1 = []
            for i in range(len(al)):
                t1.extend(duplicates[al[i]])
            t1 = list(set(t1))
            dictionary = {}
            isCandidateKey = True
            for i in range(len(t1)):
                check = []
                for j in range(len(al)):
                    check += [relation[t1[i]][al[j]]]
                if str(check) in dictionary.keys():
                    isCandidateKey = False
                    break
                else:
                    dictionary[str(check)] = True
                founded = check
            if isCandidateKey:
                candidate += [al]
        allList = []

    # print("!!", candidate)
    answer = len(candidate)


    return answer

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))