def solution(n, t, m, p):
    answer = ''
    total = p + (t-1) * m
    nums = ['0']
    i = 0
    while len(nums) < total:
        tmp = i
        converted = []
        while tmp > 0:
            d = tmp % n
            if d >= 10:
                converted = [chr(d+55)] + converted[:]
            else:
                converted = [str(d)] + converted[:]
            tmp = tmp // n
        
        nums.extend(converted)
        i += 1
    for i in range(p-1, len(nums), m):
        answer += nums[i]
        if len(answer) >= t:
            break
    
    return answer


print(solution(2, 4, 2, 1))