
class Heap:
    def __init__(self):
        self.heap_array = []
        self.heap_array.append(None)
    
    def move_up(self, index_id):
        if index_id == 1:
            return False
        
        parent_id = index_id // 2
        if self.heap_array[parent_id] > self.heap_array[index_id]:
            return True
        return False

    def move_down(self, index_id):
        left_id = index_id * 2
        right_id = index_id * 2 + 1
        if left_id >= len(self.heap_array):
            return False

        elif right_id >= len(self.heap_array):
            if self.heap_array[left_id] < self.heap_array[index_id]:
                return True
            else:
                return False
        else:
            if self.heap_array[left_id] < self.heap_array[right_id]:
                if self.heap_array[left_id] < self.heap_array[index_id]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[right_id] < self.heap_array[index_id]:
                    return True
                return False


    def insert(self, data):
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True
        
        self.heap_array.append(data)
        index_id = len(self.heap_array)-1

        while self.move_up(index_id):
            parent_id = index_id // 2
            self.heap_array[parent_id], self.heap_array[index_id] = self.heap_array[index_id], self.heap_array[parent_id]
            index_id = parent_id

        return True

    def delete(self):
        if len(self.heap_array) < 1:
            return None
        
        returned_data = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]

        index_id = 1
        while self.move_down(index_id):
            left_id = index_id * 2
            right_id = index_id * 2 + 1

            if right_id >= len(self.heap_array):
                if self.heap_array[left_id] < self.heap_array[index_id]:
                    temp = self.heap_array[left_id]
                    self.heap_array[left_id] = self.heap_array[index_id]
                    self.heap_array[index_id] = temp
                    index_id = left_id
            else :
                if self.heap_array[left_id] > self.heap_array[right_id]:
                    if self.heap_array[right_id] < self.heap_array[index_id]:
                        temp = self.heap_array[right_id]
                        self.heap_array[right_id] = self.heap_array[index_id]
                        self.heap_array[index_id] = temp
                        index_id = right_id
                    else:
                        temp = self.heap_array[left_id]
                        self.heap_array[left_id] = self.heap_array[index_id]
                        self.heap_array[index_id] = temp
                        index_id = left_id
                else:
                    if self.heap_array[left_id] < self.heap_array[index_id]:
                        temp = self.heap_array[left_id]
                        self.heap_array[left_id] = self.heap_array[index_id]
                        self.heap_array[index_id] = temp
                        index_id = left_id
                    else:
                        temp = self.heap_array[right_id]
                        self.heap_array[right_id] = self.heap_array[index_id]
                        self.heap_array[index_id] = temp
                        index_id = right_id

        return returned_data

    def check(self, limit):
        if self.heap_array[1] >= limit:
            return True
        return False

def solution(scoville, K):
    answer = 0
    h = Heap()
    for i in scoville:
        h.insert(i)

    while not h.check(K):
        q = h.delete()
        w = h.delete()
        h.insert(q + w*2)
        answer += 1

    return answer


print(solution([10,1,2,3,9,12], 7))
