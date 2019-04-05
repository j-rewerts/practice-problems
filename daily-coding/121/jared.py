# Hard
# This problem was asked by Google.
# Given a string which we can delete at most k, return whether you can make a palindrome.
# For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get 'waterretaw'.

# Determines if you can make a string a palindrome.
# O(n**3) - I feel like there's a tighter bound, but this solution
# is nowhere near optimal anyways.
def canBePalindrome(k, potential):
  start = 0
  end = len(potential) - 1
  
  while start < end:
    a, b = 0, 0
    if potential[start] != potential[end]:
      a, b = findMinMoves(start, end, potential)

    start = start + a + 1
    end = end - b - 1
    k = k - (a + b)

    if k < 0:
      return False
  return True

# a is a pointer to a character. It moves forward.
# b is a pointer to a character. It moves back.
# a < b
# We need to find the smallest number of moves
# before finding matching characters
# Ex: (a=0, b=5, word='abacde') returns (0, 3), 
# since b must move back 3.
# Note: if no solution is found, I just assign
# the worst case to 'a'. I'm not sure this is a 
# good idea.
# O(n*n)
def findMinMoves(a, b, word):
  options = []
  aIn = a
  bIn = b
  # This loops moves through a
  while aIn < bIn:
    bIn = b
    # This loops moves through b
    while aIn < bIn:
      if word[aIn] == word[bIn]:
        options.append((aIn-a, b-bIn))
      bIn -= 1
    aIn +=1
  # We've now generated all possible solutions. We must search them.
  best = (b-a, 0)
  for a, b in options:
    if a + b <= best[0] + best[1]:
      best = (a, b)

  return best

print(canBePalindrome(2, 'waterrfetawx')) # True
print(canBePalindrome(1, 'waterrfetawx')) # False
print(canBePalindrome(0, '')) # True
print(canBePalindrome(0, 'a')) # True
print(canBePalindrome(0, 'aa')) # True
print(canBePalindrome(0, 'aba')) # True
print(canBePalindrome(0, 'abca')) # False
print(canBePalindrome(1, 'abca')) # True

print(canBePalindrome(0, "waterrfetawx")) # False
print(canBePalindrome(1, "waterrfetaw")) # True
print(canBePalindrome(0, "banana")) # False
print(canBePalindrome(1, "banana")) # True
print(canBePalindrome(2, "bananad")) # True
print(canBePalindrome(1, "bananad")) # False
print(canBePalindrome(3, "bananfad")) # True
print(canBePalindrome(2, "banafad")) # False