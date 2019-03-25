# This problem was asked by Google.
# Given a word W and a string S, find all starting indices in S which are anagrams of W.
# For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.

def getIndices(word, sub):
  indices = []
  
  # Make a dict for sub
  subDict = {}
  for c in sub:
    subDict[c] = subDict.get(c, 0) + 1

  # Initialize dict for word
  wordDict = {}
  for first in range(0, len(sub)):
    wordDict[word[first]] = wordDict.get(word[first], 0) + 1

  # We handle the first index here for simplicity
  if areDictsSame(subDict, wordDict):
    indices.append(0)

  # Iterate over word len(word) - len(sub) + 1
  for first in range(1, len(word) - len(sub) + 1):
    wordDict[word[first-1]] -= 1
    # We must remove chars that aren't used
    if wordDict[word[first-1]] is 0:
      del wordDict[word[first-1]]

    last = first + len(sub) - 1
    wordDict[word[last]] = wordDict.get(word[last], 0) + 1
    
    if areDictsSame(subDict, wordDict):
      indices.append(first)
  return indices

def areDictsSame(dict1, dict2):
  if len(dict1) != len(dict2):
    return False

  for key, value in dict1.items():
    if dict2.get(key) != value:
      return False
  return True

print(getIndices('abxaba', 'ab'))
print(getIndices('abxaba', 'aa'))
print(getIndices('abxaaba', 'aa'))
print(getIndices('abaabax', 'baab'))