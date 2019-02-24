class Graph():
  def __init__(self):
    self.nodes = []
    self.dict = {}

  def get(self, name):
    if name not in self.dict:
      self.dict[name] = Node(name)
      self.nodes.append(self.dict[name])
    return self.dict[name]

  def getAll(self):
    return self.nodes

  def addEdge(self, a, b):
    start = self.get(a)
    end = self.get(b)
    start.add(end)

class Node():
  def __init__(self, name):
    self.name = name
    self.kids = []

  def add(self, node):
    self.kids.append(node)
