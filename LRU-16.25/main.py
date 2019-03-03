from queue import Queue

class Node():
  def __init__(self, value):
    self.value = value
    self.next = Node(None)
  

class LRU():
  def __init__(self, maxSize):
    self.maxSize = maxSize
    self.dict = {}
    self.tail = None
    self.head = None

  def get(self, key):
    pass
  
  def insert(self, key, value):
    node = Node(value)
    if not self.dict:
      self.dict[key] = node
      self.tail = node
      self.head = node

myCache = LRU(4)