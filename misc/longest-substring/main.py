myString = input()

mySet = set()

start = 0
maxLength = 0
for ind, c in enumerate(myString):
  if c in mySet:
    if maxLength < ind-start:
      maxLength = ind - start
    start = ind
  else:
    mySet.add(c)

print("Longest string is: " + str(maxLength))
