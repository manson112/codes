import sys

sys.setrecursionlimit(1500)

dp = [[], [""], ["0", "1"], ["00", "01", "10"]]
def find(fib, group, index):
    global dp
    if group <= 4:
        return dp[group-1][index]

    if index < fib[group-3]:
        return "0" + find(fib, group-1, index)
    else:
        return "10" + find(fib, group-2, index - fib[group-3])


fib = [1, 2]
n = int(sys.stdin.readline())

if n == 1:
    print("1")
elif n == 2:
    print("10")
else :
    while sum(fib)+1 < n:
        fib.append(fib[-1] + fib[-2])
    radix = len(fib)+1
    index = n - sum(fib[:-1]) - 2
    # print("group :", radix)
    # print("total num of this group =", fib[-1])
    # print("index of this group = ", index)
    # print(fib)
    print("10" + find(fib, radix, index))