from queue import Queue

class Node():
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.prev = None
    self.next = None
  

class LRU():
  def __init__(self, maxSize):
    self.maxSize = maxSize
    self.dict = {}
    self.tail = None
    self.head = None

  def get(self, key):
    node = self.dict[key]
    node.prev.next = node.next
    node.next.prev = node.prev
    del self.dict[key]
    
    self.head = node
    return node.value
  
  def insert(self, key, value):
    node = Node(key, value)

    if not self.dict:
      self.tail = node
      self.head = node
    else:
      node.prev = self.head
      self.head.next = node
      self.head = node

    self.dict[key] = node

    if len(self.dict) > self.maxSize:
      discard = self.tail
      self.tail = discard.next
      self.tail.prev = None
      del self.dict[discard.key]

myCache = LRU(4)
myCache.insert('key1', 1)
myCache.insert('key2', 2)
myCache.insert('key3', 3)
myCache.insert('key4', 4)
myCache.insert('key5', 5)