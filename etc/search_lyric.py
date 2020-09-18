class Tri:
    def __init__(self):
        self.children = {}        
        self.possible = {}

def solution(words, queries):
    answer = []
    root = Tri()
    reverseRoot = Tri()

    for word in words:
        cur = root
        for w in word:
            if len(word) in cur.possible:
                cur.possible[len(word)] += 1
            else :
                cur.possible[len(word)] = 1
            if w in cur.children.keys():
                cur = cur.children[w]
            else:
                cur.children[w] = Tri()
                cur = cur.children[w]
        if len(word) in cur.possible:
            cur.possible[len(word)] += 1
        else :
            cur.possible[len(word)] = 1

        cur = reverseRoot
        for i in range(len(word)-1,-1,-1):
            w = word[i]
            if len(word) in cur.possible:
                cur.possible[len(word)] += 1
            else :
                cur.possible[len(word)] = 1
            if w in cur.children.keys():
                cur = cur.children[w]
            else:
                cur.children[w] = Tri()
                cur = cur.children[w]
        if len(word) in cur.possible:
            cur.possible[len(word)] += 1
        else :
            cur.possible[len(word)] = 1
                
    for query in queries:
        if query[0] == "?":
            cur = reverseRoot
            ans = 0
            if len(query) in cur.possible:
                ans = cur.possible[len(query)]
            for i in range(len(query)-1,-1,-1):
                if query[i] == "?":
                    break
                if query[i] not in cur.children:
                    ans = 0 
                    break
                cur = cur.children[query[i]]
                if len(query) not in cur.possible:
                    ans = 0
                    break
                ans = cur.possible[len(query)]
            answer += [ans]
        else:
            cur = root
            ans = 0
            if len(query) in cur.possible:
                ans = cur.possible[len(query)]
            for i in range(len(query)):
                if query[i] == "?":
                    break
                if query[i] not in cur.children:
                    ans = 0 
                    break
                cur = cur.children[query[i]]
                if len(query) not in cur.possible:
                    ans = 0
                    break
                ans = cur.possible[len(query)]
            answer += [ans]
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))