# Easy
# This problem was asked by Google.
# Given a sorted list of integers, square the elements and give the output in sorted order.
# For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].

# When squaring our values, we will only change the ordering for the negative
# values. In a sense, we can imagine a sub-array of k values that are reverse 
# sorted. I'll sort those by converting them to positive ints, then merging 
# what was the negative half with the positive half. I'll maintain 2 pointers:
# one for the negative side and 1 for the positive.
def squareSort(ints):
  ret = [0] * len(ints)
  start = 0
  end = len(ints)-1
  insertAt = end
  while start < end:
    if ints[start]**2 > ints[end]**2:
      ret[insertAt] = ints[start]**2
      start += 1
    else:
      ret[insertAt] = ints[end]**2
      end -=1
    insertAt -= 1
  return ret

print(squareSort([-9, -2, 0, 2, 3]))
print(squareSort([1, 2, 3, 4]))
print(squareSort([-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(squareSort([-50, -20, -10]))
print(squareSort([-50, -20, -10, -5]))