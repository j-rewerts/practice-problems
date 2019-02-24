import unittest

def checkPermutation(str1, str2):
  letters = {}

  for c in str1:
    if c not in letters:
      letters[c] = 0
    letters[c] += 1

  for c in str2:
    letters[c] -= 1
  
  for c, value in letters.items():
    if value != 0:
      return False

  return True




class Test(unittest.TestCase):
  truePerms = (("abcd", "dcba"), ("trees", "stree"))
  falsePerms = (("abcd", "abc"), ("trees", "stret"))

  def test_perm(self):
    # True
    for perm in self.truePerms:
      result = checkPermutation(*perm)
      self.assertTrue(result)
      
    # False
    for perm in self.falsePerms:
      result = checkPermutation(*perm)
      self.assertFalse(result)

unittest.main()