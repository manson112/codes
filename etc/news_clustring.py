import re
import math
import json
def solution(str1, str2):
    p = re.compile('[a-z][a-z]')
    A = []
    B = []
    for i in range(len(str1)-1):
        s = str1[i:i+2].lower()
        if p.match(s):
            A += [s]
    for i in range(len(str2)-1):
        s = str2[i:i+2].lower()
        if p.match(s):
            B += [s]

    if len(A) == 0 and len(B) == 0:
        return 65536
    intersection = []    

    tmpA = json.loads(json.dumps(A))
    tmpB = json.loads(json.dumps(B))
    for i in range(len(tmpA)):
        for j in range(len(tmpB)):
            if tmpA[i] == tmpB[j]:
                intersection += [tmpB[j]]
                tmpB.pop(j)
                break
    
    tmpA.extend(tmpB)
    union = tmpA

    return math.floor(len(intersection)/len(union)*65536)

print(solution("aa aa ab ab ba", "aa ab ab ac ad"))

# fr ra an nc ce / fr re en nc ch