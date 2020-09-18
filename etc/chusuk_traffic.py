# 누적 합

def toMili(time) :
    sTime = time.split(":")
    miliTime = float(sTime[0]) * 60 * 60 * 1000 + float(sTime[1]) * 60 * 1000 + float(sTime[2].split(".")[0]) * 1000 + float(sTime[2].split(".")[1])
    return int(miliTime)

def solution(lines):
    answer = 0
    times = []
    if len(lines) == 1 :
        return 1

    for line in lines:
        sLine = line.split(" ")
        endTime = sLine[1]
        miliEndTime = toMili(endTime)
        miliDuration = int(float(sLine[2][:-1]) * 1000)
        miliStartTime = miliEndTime - miliDuration + 1
        times += [[miliStartTime, miliEndTime]]
    sorted_times = sorted(times, key=lambda x: (x[0], x[1]))
    minimum = sorted_times[0][0]
    for i in range(len(sorted_times)):
        sorted_times[i][0] -= minimum
        sorted_times[i][1] -= minimum

    cur = 0

    while cur < len(sorted_times):
        s1, e1 = sorted_times[cur][0]-999, sorted_times[cur][0]
        s2, e2 = sorted_times[cur][0], sorted_times[cur][0]+999
        s3, e3 = sorted_times[cur][1]-999, sorted_times[cur][1]
        s4, e4 = sorted_times[cur][1], sorted_times[cur][1]+999

        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        for i in range(len(sorted_times)):
            if not(sorted_times[i][1] < s1 or e1 < sorted_times[i][0]) :
                count1 += 1
            if not(sorted_times[i][1] < s2 or e2 < sorted_times[i][0]) :
                count2 += 1
            if not(sorted_times[i][1] < s3 or e3 < sorted_times[i][0]) :
                count3 += 1
            if not(sorted_times[i][1] < s4 or e4 < sorted_times[i][0]) :
                count4 += 1
        
        
        answer = max(count1, answer)
        answer = max(count2, answer)
        answer = max(count3, answer)
        answer = max(count4, answer)

        cur += 1
        



    return answer


print(solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]))