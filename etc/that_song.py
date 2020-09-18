import re

def strToMin(s):
    t = s.split(":")
    return int(t[0])*60 + int(t[1])
def solution(m, musicinfos):
    answer = ''

    p = re.compile("[A-G]#*")
    l = p.findall(m)

    a = []
    for i in range(len(musicinfos)):
        music = musicinfos[i].split(",")
        playTime = strToMin(music[1]) - strToMin(music[0])
        notes = p.findall(music[3])
        playedNotes = []
        name = music[2]
        tmp = playTime
        while tmp > 0:
            if tmp > len(notes):
                playedNotes.extend(notes)
            else:
                playedNotes.extend(notes[:tmp])
            tmp -= len(notes)

        if playTime < len(l):
            continue

        for k in range(len(playedNotes) - len(l) + 1):
            thisSong = True
            for j in range(len(l)):
                if l[j] != playedNotes[k+j]:
                    thisSong = False
                    break
            if thisSong:
                a += [[i, name, playTime]]

    if len(a) == 0:
        answer = '(None)'
    elif len(a) != 1:
        a = sorted(a, key= lambda x: x[2])
        print(a)
        b = [item for item in a if item[2] == a[-1][2]] 
        print(b)
        b = sorted(b, key= lambda x: x[0])         
        answer = b[0][1]
    else:
        answer = a[0][1]
    
    return answer

print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))