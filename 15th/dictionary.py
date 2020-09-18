import sys
import pprint
from itertools import permutations
from math import comb

sys.setrecursionlimit(10**6)

N, M, K = map(int, sys.stdin.readline().split(" "))

dp = [[-1 for _ in range(M+1)] for _ in range(N+1)]
word = ''
def possibleNumOfWord(N, M):
    global dp
    if N == 0 or M == 0: return 1
    if dp[N][M] != -1: return dp[N][M]

    dp[N][M] = min(possibleNumOfWord(N-1, M)+possibleNumOfWord(N, M-1), 1000000000+1)
    return dp[N][M]

def getWord(N, M, skip):
    global word
    if N == 0:
        for i in range(M):
            word += 'z'
        return
    if M == 0:
        for i in range(N):
            word += 'a'
        return
    idx = possibleNumOfWord(N-1, M)
    print(skip, idx)
    print(word)
    if skip < idx:
        word += 'a'
        getWord(N-1, M, skip)
    else:
        word += 'z'
        getWord(N, M-1, skip-idx)
    
            
noWord = False
if (K > possibleNumOfWord(N, M)): noWord = True
else : getWord(N, M, K-1)
if noWord : print(-1)
else : print(word)

# totalNum = comb(N+M, M)
# print(totalNum)
# if K > totalNum:
#     print(-1)
#     exit()
# if M == 1:
#     print(format(2**(K-1), '0'+str(M+N)+'b').replace("0", "a").replace("1", "z"))
#     exit()
# if N == 1:
#     print(format(2**(N+M)-1 - 2**(N+M-K), '0'+str(M+N)+'b').replace("0", "a").replace("1", "z"))
#     exit()




