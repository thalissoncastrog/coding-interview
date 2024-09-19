def strStr(self, haystack: str, needle: str) -> int:

    needleSize = len(needle)
    haystackSize = len(haystack)
    
    if needleSize == 0:
        return 0
    
    for i in range(haystackSize + 1 - needleSize):
        for j in range(needleSize):
            word = haystack[i + j]
            print(word, needle[j])
            if word != needle[j]:
                break
            if j == needleSize - 1:
                return i
    
    return -1

haystack = "leetcode"
needle = "leet"

result = strStr(None, haystack, needle)

print(result)
