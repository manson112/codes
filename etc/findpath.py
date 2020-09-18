# 
import sys 
sys.setrecursionlimit(10**6) 
class Node:
    def __init__(self, num, l):
        self.num = num
        self.x = l[0]
        self.y = l[1]

    def __str__(self):
        return "N({}, {})".format(self.x, self.y)
    def __repr__(self):
        return str(self)

def preFix(root, level, leftList, rightList, sortedLevel, index, prefix, postfix):
    prefix += [root.num]
    
    if index >= len(sortedLevel):
        postfix += [root.num]
        return

    if len(leftList) != 0:
        lRoot = [x for x in leftList if x.y == sortedLevel[index]][0]
        ll = [x for x in leftList if x.x < lRoot.x]
        lr = [x for x in leftList if x.x > lRoot.x]
        preFix(lRoot, level, ll, lr, sortedLevel, index+1, prefix, postfix)

    if len(rightList) != 0:
        rRoot = [x for x in rightList if x.y == sortedLevel[index]][0]
        rl = [x for x in rightList if x.x < rRoot.x]
        rr = [x for x in rightList if x.x > rRoot.x]
        preFix(rRoot, level, rl, rr, sortedLevel, index+1, prefix, postfix)
    
    postfix += [root.num]


  
def preFixContainer(level, nodes):
    sortedIndex = sorted(level, reverse=True)
    left = [v for k, v in nodes.items() if v.x < nodes[level[sortedIndex[0]][0]].x] 
    right = [v for k, v in nodes.items() if v.x > nodes[level[sortedIndex[0]][0]].x] 
    prefix = []
    postfix = []
    preFix(nodes[level[sortedIndex[0]][0]], level, left, right, sortedIndex, 1, prefix, postfix)
    return prefix, postfix

def solution(nodeinfo):
    answer = []
    
    level = {}
    nodes = {}
    for i in range(len(nodeinfo)):
        if nodeinfo[i][1] in level:
            level[nodeinfo[i][1]] += [i+1]
        else:
            level[nodeinfo[i][1]] = [i+1]

        nodes[i+1] = Node(i+1, nodeinfo[i])
    answer += preFixContainer(level, nodes)

    return answer

print(solution([[5,3]]))