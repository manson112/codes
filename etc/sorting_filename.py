import re
def solution(files):
    answer = []
    p = re.compile("[0-9]{1,5}")
    dictionary = []
    for i in range(len(files)):
        m = p.search(files[i])
        head = files[i][:m.start()]
        num = int(m.group())
        tail = files[i][m.end():]
        dictionary += [[i, head.lower(), num]]

    dictionary = sorted(dictionary, key= lambda x: (x[1], x[2], x[0]))
    for d in dictionary :
        answer += [files[d[0]]]
    return answer

print(solution(["i00012345mg12.png", "i100235mg10.png", "i122341mg02.png", "i343455mg1.png", "I6542345MG01.GIF", "i266632mg2.JPG"]))