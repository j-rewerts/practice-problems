import graph

projects = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
depend = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c'), ('g', 'a'), ('a', 'c')]

def buildGraph(projects, depend):
  graph = Graph()
  for project in projects:
    graph.get(project)
  
  for a, b in depend:
    graph.addEdge(a, b)
  return graph

def getPackageOrder(graph, pros, deps):
  

ret = getBuildOrder(projects, depend)
print(ret)