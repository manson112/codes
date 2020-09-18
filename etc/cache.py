# LRU cache

def findFromCache(cache, city, cacheSize):
    try :
        index = cache.index(city)
        cache.pop(index)
        cache += [city]
        return True
    except:
        cache += [city]
        if len(cache) > cacheSize :
            cache.pop(0)
        return False

def solution(cacheSize, cities):
    answer = 0
    cache = []
    for c in cities:
        if findFromCache(cache, c.lower(), cacheSize):
            answer += 1
        else :
            answer += 5
    return answer

print(solution(30, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))