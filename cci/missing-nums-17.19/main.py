import math
from functools import reduce

def getMissing2(n, values):
  mult = math.factorial(n)/reduce(lambda x, y: x*y, values)
  add = sum(range(n+1))-sum(values)

  a1 = (add + math.sqrt(add**2 - 4*mult)) / 2
  a2 = (add - math.sqrt(add**2 - 4*mult)) / 2
  return (a1, a2)

print(getMissing2(15, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14]))