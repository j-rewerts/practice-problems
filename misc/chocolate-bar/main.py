def getSubsets(bar, numFriends):
  if numFriends == 0:
    return []
  segSweet = []
  totalSweet = sum(bar)
  avgSweet = totalSweet/numFriends
  cSweet = 0

  for ind, elem in enumerate(bar):
    if abs(cSweet + elem - avgSweet) < abs(cSweet - avgSweet):
      cSweet += elem
    else:
      segSweet.append(cSweet)
      return segSweet + getSubsets(bar[ind:], numFriends-1)
  return segSweet

# Runs in O(n)
def getSubsetsBetter(bar, numFriends):
  segSweet = []
  totalSweet = sum(bar)
  avgSweet = totalSweet/numFriends
  cSweet = 0

  for ind, elem in enumerate(bar):
    if abs(cSweet + elem - avgSweet) < abs(cSweet - avgSweet):
      cSweet += elem
    else:
      segSweet.append(cSweet)
      cSweet = elem
      totalSweet = sum(bar[ind:])
      avgSweet = totalSweet/(numFriends-len(segSweet))
  segSweet.append(cSweet)
  return segSweet

def getMinSubsets(bar, numFriends):
  subsets = getSubsetsBetter(bar, numFriends)
  return min(subsets)

bar1 = [1, 2, 3, 3, 2, 4, 4, 4, 11]
print(getMinSubsets(bar1, 3))