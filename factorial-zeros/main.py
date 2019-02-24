# Cracking the Coding Interview, Question 16.5
# @author CodyGramlich and j-rewerts
# Calculates the number of zeros in n factorial.


def howManyFives(num):
  fives = 0
  while num % 5 == 0:
    num = num / 5
    fives += 1
  return fives

def factZeros(n):
  fives = 0
  for i in range(5, n+1, 5):
    fives += howManyFives(i)
  return fives

print(factZeros(125))