def solution(n, t, m, timetable):
    answer = ''
    bus = [540+i*t for i in range(n)]
    a = bus[-1] # 마지막 버스 도착 시간
    passenger = sorted([int(a.split(":")[0])*60+int(a.split(":")[1]) for a in timetable])
    lastBus = bus[-1]
    restIndex = 0
    for b in bus:
        # 현재 버스 정원
        curM = m
        for i in range(restIndex, len(passenger)):
            # 탑승
            if passenger[i] <= b:
                curM -= 1
            # 버스가 다 차지않았으나 승객이 아직 오지 않음
            else:
                restIndex = i 
                # 버스가 다 차지 않았으므로 이 시간에 오면 탈 수 있음
                a = b
                break
            # 가득 참
            if curM == 0:   
                # 다음 탑승 승객 index
                restIndex = i+1
                # 마지막 버스라면
                if b == lastBus:
                    # 마지막 승객 시간 -1분
                    a = passenger[i]-1
                break
    answer = "{:02d}:{:02d}".format(a//60, a%60)

    return answer

print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))