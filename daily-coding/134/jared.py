# Facebook - easy
# You have a large array with most of the elements as zero.
# Use a more space efficient data structure, SparseArray, 
# that implements the same interface.
#   - init(arr, size): initialize with the original large 
#     array and size.
#   - set(i, val): updates index at i with val.
#   - get(i): gets the value at index i.

class SparseArray:
  def __init__(self, arr, size):
    self.dict = {}
    self.size = size
    self.initialize(arr)

  def initialize(self, arr):
    for index, element in enumerate(arr):
      self.dict[index] = element

  def set(self, index, value):
    if index >= self.size:
      self.size = index + 1
    self.dict[index] = value

  def get(self, index):
    if index >= self.size:
      raise AttributeError()
    return self.dict.get(index, 0)

arr = [0, 0, 0, 0, 0, 1, 0, 0]
sparseArray = SparseArray(arr, len(arr))
print(sparseArray.get(4))
print(sparseArray.get(5))
print(sparseArray.get(6))
sparseArray.set(4, 1)
print(sparseArray.get(4))
print(sparseArray.get(5))
print(sparseArray.get(6))