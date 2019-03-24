def add(num1, num2):
  bin1 = bin(num1)[2:]
  bin2 = bin(num2)[2:]

  larger = max(len(bin1), len(bin2))
  bin1 = bin1.rjust(larger, '0')
  bin2 = bin2.rjust(larger, '0')

  # print('Bin1 ' + bin1)
  # print('Bin2 ' + bin2)
  addedValue = list('0' * len(bin1))
  carryOver = 0
  ind = len(bin1)-1
  # print(addedValue)
  for c1, c2 in zip(reversed(bin1), reversed(bin2)):
    c1 = int(c1)
    c2 = int(c2)
    # print ((c1, c2))
    if bool(c1) and bool(c2) and bool(carryOver):
      addedValue[ind] = 1
      carryOver = 1
    elif bool(c1) and bool(c2) and not bool(carryOver):
      addedValue[ind] = 0
      carryOver = 1
    elif (bool(c1) != bool(c2)) and bool(carryOver):
      addedValue[ind] = 0
      carryOver = 1
    elif (bool(c1) != bool(c2)) and not bool(carryOver):
      addedValue[ind] = 1
      carryOver = 0
    elif not bool(c1) and not bool(c2) and bool(carryOver):
      addedValue[ind] = 1
      carryOver = 0
    else:
      addedValue[ind] = 0
      carryOver = 0
    ind = ind - 1
  # print(addedValue)
  binaryString = ''.join(map(str, addedValue))
  if carryOver:
    binaryString = '1' + binaryString
  # print(binaryString)
  print(int(binaryString, 2))

add(1, 1)
add(1, 2)
add(2, 1)
add(2, 2)
add(2, 3)
add(5, 13)