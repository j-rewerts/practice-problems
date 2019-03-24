from queue import Queue


def getBuildOrder(pro, deps):
    nodes = Queue()
    parents = set()
    children = set()
    adjList = {}
    for parent, child in deps:
        parents.add(parent)
        children.add(child)
        if parent not in adjList:
            adjList[parent] = [child]
        else:
            adjList[parent].append(child)

    # find disconnected
    all = parents.union(children)
    for project in pro:
        if project not in all:
            nodes.put(project)

    roots = parents.difference(children)
    for root in roots:
        nodes.put(root)
    return explore(nodes, adjList)


def explore(roots, adjList):
    order = []
    visited = set()
    while not roots.empty():
        root = roots.get()
        if root not in visited:
          order.append(root)
        visited.add(root)
        if root in adjList:
          for node in adjList[root]:
              if node in visited:
                  return False
              roots.put(node)
    return order

projects = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
depend = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c'), ('g', 'a'), ('a', 'c')]
ret = getBuildOrder(projects, depend)
print(ret)