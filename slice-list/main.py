import itertools as it

def skipI(iterable, i):
  itr = iter(iterable)
  return it.chain(it.islice(itr, 0, i), it.islice(itr, 1, None))

listA = ['A', 'B', 'C', 'D', 'E']
listMod1 = skipI(listA, 1)
listMod2 = skipI(listMod1, 1)

for elem in listMod2:
  print(elem)