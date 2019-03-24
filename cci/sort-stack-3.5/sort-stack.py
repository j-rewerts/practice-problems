import unittest

def sortStack(stack):
  ignorePast = 999999

  sorted = False
  while not sorted:
    sorted, ignorePast = moveLargest(stack, ignorePast)
  
  return stack

def moveLargest(stack, ignorePast=99999):
  flippedStack = []
  biggest = -999999

  if ignorePast == stack[-1]:
    return True, biggest

  while stack and stack[-1] < ignorePast:
    value = stack.pop()
    if value > biggest:
      if biggest != -999999:
        flippedStack.append(biggest)
      biggest = value
    else:
      flippedStack.append(value)
  stack.append(biggest)

  while flippedStack:
    stack.append(flippedStack.pop())
  return False, biggest


class Test(unittest.TestCase):
  stackA = [1, 2, 0, 5, 4, 3]
  stackASorted = [5, 4, 3, 2, 1, 0]

  def test_StackSort(self):
    sortedStack = sortStack(self.stackA)
    self.assertListEqual(sortedStack, self.stackASorted)

unittest.main()