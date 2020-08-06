import pprint
test_case = int(input())

for c in range(test_case):
    n = int(input())

    mmap = []
    for i in range(n):
        line = input()
        l = []
        for j in range(n):
            l += [int(line[j])]
        mmap += [l]

    score = [[1000000000 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(n):
        for j in range(n):
            score[i][j] = min(mmap[i][j])

    print("#", c+1, " ", score[0][0], sep='')    