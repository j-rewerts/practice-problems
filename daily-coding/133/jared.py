# Amazon - easy
# Given a node in a binary search tree, return the
# next bigger element, also known as the inorder successor.
# 
# For example, the inorder successor of 22 is 30.
#
#   10
#  /  \
# 5   30
#    /  \
#   22  35
#
# You can assume each node has a parent pointer.

# Gets the next node larger. If no such node exists, return None.
def getSuccessor(node):
  if node.right:
    return getSmallest(node.right)
  elif node.parent and node.parent.left is node:
    return node.parent
  return None

# Finds the smallest node in a tree rooted at node.
def getSmallest(node):
  if node.left:
    return getSmallest(node.left)
  else:
    return node

class Node:
  left = None
  right = None

  def __init__(self, value, parent=None):
    self.value = value
    self.parent = parent

root = Node(10)
node1 = Node(5, root)
root.left = node1
node2 = Node(30, root)
root.right = node2
node3 = Node(22, node2)
node2.left = node3
node4 = Node(35, node2)
node2.right = node4

print("Successor of 5 is " + str(getSuccessor(node1).value))
print("Successor of 10 is " + str(getSuccessor(root).value))
print("Successor of 22 is " + str(getSuccessor(node3).value))
print("Successor of 30 is " + str(getSuccessor(node2).value))
print("Successor of 35 is " + str(getSuccessor(node4)))