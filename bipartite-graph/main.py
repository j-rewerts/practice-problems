nodes = [[1,3], [0,2], [1,3], [0,2]]
otherNodes = [[1,2,3], [0,2], [0,1,3], [0,2]]

def isBipartite(nodes):
  colors = [0] * len(nodes)
  for index, node in enumerate(nodes):
    if colors[index] == 0 and not properColor(nodes, colors, 1, index):
      return False
  return True

def properColor(graph, colors, color, nodeNum):
  if colors[nodeNum] != 0:
    return colors[nodeNum] == color
  colors[nodeNum] = color
  for children in graph[nodeNum]:
    if not properColor(graph, colors, -color, children):
      return False
  return True

print(isBipartite(nodes))
print(isBipartite(otherNodes))