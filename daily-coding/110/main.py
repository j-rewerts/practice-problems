# This problem was asked by Facebook.
# Given a binary tree, return all paths from the root to leaves.
# For example, given the tree:
#    1
#   / \
#  2   3
#     / \
#    4   5
# Return [[1, 2], [1, 3, 4], [1, 3, 5]].

def getPaths(tree, path):
  left = None
  if tree.left:
    left = getPaths(tree.left, path + [tree.value])
  right = None
  if tree.right:
    right = getPaths(tree.right, path + [tree.value])

  mergedList = []
  if left:
    mergedList = mergedList + left
  if right:
    mergedList = mergedList + right
  
  if len(mergedList) > 0:
    return mergedList
  else:
    return [path + [tree.value]]


  

class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

two = Node(2)
four = Node(4)
five = Node(5)
three = Node(3)
three.left = four
three.right = five
one = Node(1)
one.left = two
one.right = three

print(getPaths(one, []))