def solution(record):
    answer = []
    
    dic = {}
    ops = []
    for i in range(len(record)):
        arr = record[i].split(" ")
        
        if arr[0] == "Enter":
            dic[arr[1]] = arr[2]
            ops += [[arr[1], "님이 들어왔습니다."]]
        elif arr[0] == "Leave":
            ops += [[arr[1], "님이 나갔습니다."]]
        else:
            dic[arr[1]] = arr[2]
    
    for op in ops:
        answer += [dic[op[0]] + op[1]]

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))