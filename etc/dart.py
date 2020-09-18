# 정규표현식
import re

def solution(dartResult):
    answer = 0
    p = re.compile("[0-9]+[SDT][*#]?")

    prev = 0
    for result in p.findall(dartResult):
        score, b, o = 0, 'S', ''
        try:
            score = int(result[:2])
        except:
            score = int(result[0])
        
        if result[-1] == "*" or result[-1] == "#":
            b = result[-2]
        else:
            b = result[-1]
        o = result[-1]

        if b == 'D':
            score = score ** 2
        elif b == 'T':
            score = score ** 3
        
        if len(result) == 3:
            if o == '*':
                prev *= 2
                score *= 2 
            elif o == '#':
                score *= -1
        answer += prev
        prev = score
    answer += prev
    return answer

print(solution(	"10S10D*10T"))