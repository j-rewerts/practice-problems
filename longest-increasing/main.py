inputStrings = input().split(' ')
values = list(map(int, inputStrings))

start = 0
lastValue = 0
maxLength = 0
for ind, value in enumerate(values):
  if lastValue < value:
    lastValue = value
  else:
    start = ind

  if maxLength < ind - start + 1:
      maxLength = ind - start + 1

print(maxLength)