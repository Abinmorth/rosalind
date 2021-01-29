import READ_FASTA

def getShortestString(array):
    length = 1001
    shortest = ''
    for s in array:
        l = len(s)
        if l < length:
            shortest = s
            length = l
    return (shortest, length)

def findLcs(array):
    (shortestString, shortestLen) = getShortestString(array)
    shortestLen = len(shortestString)
    for k in range(shortestLen, 0, -1):
        for i in range(k, shortestLen + 1):
            substringToCheck = shortestString[i-k:i]
            if checkIfLCS(substringToCheck, array):
                return substringToCheck

def checkIfLCS(substring, data):
    for s in data:
        if substring not in s:
            return 0
    return 1

data = READ_FASTA.read_fasta('lcsm_in.txt')
lcs = findLcs(data.values())
print(lcs)
    
