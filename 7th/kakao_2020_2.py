
def dist(d1, d2):
    return abs(d1[0]-d2[0]) + abs(d1[1]-d2[1])

def solution(numbers, hand):
    answer = ''
    LCur = [3, 0]
    RCur = [3, 2]

    for i in range(len(numbers)):
        if numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7:
            answer += "L"
            LCur = [numbers[i]//3, 0]
        elif numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9:
            answer += "R"
            RCur = [(numbers[i]-1)//3, 2]
        else:
            destination = [0, 1]
            if numbers[i] == 0:
                destination = [3, 1]
            else:
                destination = [numbers[i]//3, 1]
            if dist(LCur, destination) < dist(RCur, destination):
                answer += "L"
                LCur = destination
            elif dist(LCur, destination) > dist(RCur, destination):
                answer += "R"
                RCur = destination
            else :
                if hand == "right":
                    answer += "R"
                    RCur = destination
                else :
                    answer += "L"
                    LCur = destination
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))