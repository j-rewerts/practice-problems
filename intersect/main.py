# Cracking the coding interview. Question 16.3.
# @author CodyGramlich and j-rewerts
# Finds the intersection between 2 lines.

def intersect(i1, i2, j1, j2):
  xInt = 0
  yInt = 0
  if i1[0] == i2[0] and j1[0] == j2[0]:
    print('Lines are vertical.')
    return None
  elif i1[0] == i2[0]:
    mj = (j2[1] - j1[1]) / (j2[0] - j1[0])
    bj = j2[1] - mj * j2[0]
    xInt = i1[0]
    yInt = mj * xInt + bj
  elif j1[0] == j2[0]:
    mi = (i2[1] - i1[1]) / (i2[0] - i1[0])
    bi = i2[1] - mi * i2[0]
    xInt = j1[0]
    yInt = mi * xInt + bi
  else:
    mi = (i2[1] - i1[1]) / (i2[0] - i1[0])
    bi = i2[1] - mi * i2[0]

    mj = (j2[1] - j1[1]) / (j2[0] - j1[0])
    bj = j2[1] - mj * j2[0]

    if mi - mj == 0:
      print('No intercept')
      return None

    xInt = (bj - bi) / (mi - mj)
    yInt = mi * xInt + bi
  if checkBounds(i1, i2, (xInt, yInt)) and checkBounds(j1, j2, (xInt, yInt)):
    return (xInt, yInt)
  else:
    print('Intersects beyond line segments.')
    return None

def checkBounds(i1, i2, p):
  if i1[0] <= p[0] <= i2[0] and i1[1] <= p[1] <= i2[1]:
    return True
  return False

print('Bounds tests')
print(checkBounds((0,0), (2,2), (1,1)))
print(checkBounds((0,0), (2,2), (3,1)))

print('')
print('Intersection tests')
# Standard intersection test
print(intersect((1, 1), (3, 2), (1, 0), (2, 4)))
# Standard intersect, but out of bounds
print(intersect((1, 1), (2, 2), (0, 5), (5, 0)))
# First line is vertical, intersects
print(intersect((1.5, 1), (1.5, 4), (1, 0), (2, 4)))
# First line is vertical, and is out of bounds
print(intersect((0, 1), (0, 2), (1, 0), (2, 4)))

# Second line is vertical and intersects
print(intersect((1, 1), (4, 4), (2, 0), (2, 4)))
# Second line is vertical and is out of bounds
print(intersect((1, 1), (4, 4), (5, 0), (5, 4)))
# Both lines are vertical
print(intersect((1, 1), (1, 4), (2, 0), (2, 4)))
# Lines are parallel
print(intersect((1, 1), (4, 4), (1, 0), (4, 3)))