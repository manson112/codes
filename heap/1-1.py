import heapq


def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)
    q = heapq.heappop(scoville)
    w = heapq.heappop(scoville)

    while(q < K):
        heapq.heappush(scoville, q + 2*w)
        answer += 1
        if len(scoville) == 1:
            if scoville[0] < K:
                return -1
            else:
                return answer
        else :
            q = heapq.heappop(scoville)
            w = heapq.heappop(scoville)

    return answer


print(solution([10,1], 7))
