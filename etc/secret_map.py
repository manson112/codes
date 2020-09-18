def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        num = arr1[i] | arr2[i]
        s = ""
        for j in range(n):
            s += "#" if num & (2**(n-1) >> j) else " "
        answer += [s]
    return answer

def s(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        answer += [str(bin(i|j)[2:]).replace("1","#").replace("0", " ")]
    return answer

print(s(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))