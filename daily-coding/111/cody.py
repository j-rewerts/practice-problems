def findIndices(S, W):
    indices = []
    length = len(W)
    for i in range(len(S) - len(W) + 1):
        A = S[i:i+length]
        if set(A) == set(W):
            indices.append(i)
    return indices

def getIndices(word, sub):
    indices = []
    subDict = {}
    for char in sub:
        subDict[char] = subDict.get(char, 0) + 1

    length = len(sub)
    for i in range(len(word) - len(sub) + 1):
        wordDict = {}
        for j in range(i, i+length):
            char = word[j]
            wordDict[char] = wordDict.get(char, 0) + 1

        if wordDict == subDict:
            indices.append(i)

    return indices

print('findIndices')
print(findIndices('abxaba', 'ab'))
print(findIndices('abxaba', 'aa'))
print(findIndices('abxaaba', 'aa'))
print(findIndices('abaabax', 'baab'))

print('getIndices')
print(getIndices('abxaba', 'ab'))
print(getIndices('abxaba', 'aa'))
print(getIndices('abxaaba', 'aa'))
print(getIndices('abaabax', 'baab'))