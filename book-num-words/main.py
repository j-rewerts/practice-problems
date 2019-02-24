
def getFrequency(book):
  words = book.split()
  wordFreq = {}
  for word in words:
    if word not in wordFreq:
      wordFreq[word] = 0
    wordFreq[word] += 1
  return wordFreq

book1 = 'this is a test. Tests are fun, but they can be tricky. A bit tricky for a sure.'
print(getFrequency(book1))