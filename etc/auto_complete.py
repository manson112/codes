class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
        self.possible_word = 0

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cur_node = self.head
        for c in string:
            if c not in cur_node.children:
                cur_node.children[c] = Node(c)
            cur_node.possible_word += 1
            cur_node = cur_node.children[c]
        
        cur_node.possible_word += 1
        cur_node.data = string

    def search(self, string):
        cur_node = self.head
        result = ''
        for c in string:
            if c in cur_node.children:
                cur_node = cur_node.children[c]
                result += c
                if cur_node.possible_word == 1:
                    return result
            else:
                return result
        return result

    def starts_with(self, prefix):
        # print("==========", prefix)
        cur_node = self.head
        result = []
        subTrie = None

        for c in prefix:
            if c in cur_node.children:
                cur_node = cur_node.children[c]
                subTrie = cur_node
            else:
                return None

        if cur_node.data != None:
            result.append(cur_node.data)
        
        queue = list(subTrie.children.values())
        while queue:
            cur = queue.pop()
            if cur.data != None:
                result.append(cur.data)

            queue += list(cur.children.values())
        return result
    def show(self):
        cur_node = self.head
        queue = []
        while len(cur_node.children) != 0:
            # print("CUR:", cur_node.key)
            for k in cur_node.children:
                # print(k, end=" / ")
                queue.append(cur_node.children[k])
            # print()
            cur_node = queue.pop(0)

    
def solution(words):
    answer = 0
    tri = Trie()
    
    for i in range(len(words)):
        tri.insert(words[i])
    
    for i in range(len(words)):
        match = tri.search(words[i])
        answer += len(match)
    return answer

print(solution(	["word", "war", "warrior", "world"]))