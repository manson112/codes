from itertools import permutations
import copy

def calculate(o1, op, o2):
    if op == "+" : return o1+o2
    elif op == "-" : return o1-o2
    else: return o1*o2

def calc(n, o, cur) :
    i = 0
    while i < len(o):
        if o[i] == cur:
            res = calculate(n[i], cur, n[i+1])
            del o[i]
            del n[i:i+2]
            n.insert(i, res)
            i -= 1
        i += 1

def solution(expression):
    answer = 0

    op = ["+", "*", "-"]
    perm = permutations(op)

    nums = []
    ops = []

    last = 0
    for i in range(len(expression)):
        if expression[i] == "-" or expression[i] == "+" or expression[i] == "*":
            nums += [int(expression[last:i])]
            ops += [expression[i:i+1]]
            last = i+1
    nums += [int(expression[last:])]

    for i in list(perm):
        ns = copy.deepcopy(nums)
        os = copy.deepcopy(ops)
        for j in i:
            calc(ns, os, j)
        answer = max(answer, abs(ns[0]))
    return answer


print(solution("50*6-3*2"))