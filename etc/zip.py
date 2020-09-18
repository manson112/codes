def solution(msg):
    answer = []
    dictionary = [chr(ord('A')+i) for i in range(26)]

    done = False
    word = ''
    start = 0
    while start < len(msg):
        word += msg[start]
        try :
            index = dictionary.index(word)
            start += 1
            if start == len(msg):
                answer += [index+1]
            continue
        except:
            dictionary += [word]
            index = dictionary.index(word[:-1])
            answer += [index+1]
            word = ''

    return answer
print(solution("TOBEORNOTTOBEORTOBEORNOT"))