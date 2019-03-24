# A circular array implementation
# Based on CCI 7.9
# @author j-rewerts

class CircularArray:
  def __init__(self, myList):
    self.ind = 0
    self.list = myList
  
  def __iter__(self):
    for times in range(len(self.list)):
      index = (times + self.ind) % len(self.list)
      yield self.list[index]

  def rotate(self, amount):
    self.ind = (self.ind + amount) % len(self.list)

print('Test 1')
circ = CircularArray([1, 2, 3, 4])
for val in circ:
  print(val)

print('Test 2')
circ.rotate(1)
for val in circ:
  print(val)

print('Test 3')
circ.rotate(-1)
for val in circ:
  print(val)

print('Test 4')
circ.rotate(-1)
for val in circ:
  print(val)