def findIndices(S, W):
    indices = []
    length = len(W)
    for i in range(len(S)):
        A = S[i:i+length]
        if set(A) == set(W):
            indices.append(i)
    return indices

print(findIndices('abxaba', 'ab'))
print(findIndices('abxaba', 'aa'))
print(findIndices('abxaaba', 'aa'))