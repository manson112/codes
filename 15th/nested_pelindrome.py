import sys
import json
sys.setrecursionlimit(10**6)

half = []
answer = []

def isPelindrome(s):
    check = True
    for i in range(len(s)//2):
        if s[len(s)-1-i] == "?":
            continue
        if s[i] != s[len(s)-1-i]:
            check = False
    return check

def halfPelindrome(s, index):
    global half
    # print("S = {}".format(s))
    # print("index= {}".format(index))
    if s[0] == "0":
        return 
    if index >= len(s):
        half += [s]
        return 

    if s[index] != "?":
        halfPelindrome(s, index+1)
    else :
        start = 0
        if index == 0: start = 1
        if index <= len(s)//2:
            for i in range(start, 10):
                if index - 1 >= 0:
                    if s[index-1] == str(i):
                        continue
                if index + 1 < len(s):
                    if s[index+1] == str(i):
                        continue
                tmp = json.loads(json.dumps(s))
                tmp[index] = str(i)
                halfPelindrome(tmp, index+1)
        else:
            tmp = json.loads(json.dumps(s))
            tmp[index] = tmp[len(tmp)-1-index]
            halfPelindrome(tmp, index+1)
    
while True:
    k = int(sys.stdin.readline())
    if k == 0:
        break
    answer = []
    half = []
    str_num = list(sys.stdin.readline().rstrip())
    if str_num[0] == "0" or len(str_num) % 2 == 0:
        print(-1)
        continue
    if len(str_num) == 1:
        if str_num[0] == "?":
            print(k)
        else:
            if k > 1 : 
                print(-1)
            else:
                print(str_num[0])
        continue
    n = 1
    for i in range(len(str_num)//2):
        if str_num[i] == "?":
            n *= 9
    if len(str_num) % 2 == 1 and str_num[len(str_num)//2] == "?":
        n *= 9
    if k > n:
        print(-1)
        continue
    
    halfPelindrome(str_num[:len(str_num)//2], 0)
    # print("half=",half)
    for i in range(len(half)):
        tmp = half[i][:] + str_num[len(str_num)//2:]
        # print(tmp)
        if not isPelindrome(tmp):
            print(-1)
        else :
            if tmp[len(tmp)//2] != "?":
                # print("here")
                if half[-1] != tmp[len(tmp)//2]:
                    t = half[i][:]
                    t.reverse()
                    answer += [tmp[:len(str_num)//2+1] + t]
                    # print("answer:", answer)
                if len(answer) >= k:
                    print(''.join(answer[k-1]))
                    break
                continue
            if k > 9:            
                k -= 9
                continue
            t = half[i][:]
            t.reverse()
            if tmp[len(tmp)//2] == "?":
                for j in range(10):
                    if tmp[len(tmp)//2] != str(j):
                        tmp2 = half[i][:] + [str(j)] + t
                        answer += [tmp2]
                print(''.join(answer[k-1]))
                break       
            else:
                tmp2 = half[i][:] + [str(j)] + t
                answer += [tmp2]