inputVal = input()
intList = [int(x) for x in inputVal]

print(intList)
intList.sort(reverse=True)
print(intList)
stringList = [str(x) for x in intList]
print(''.join(stringList))