import hashlib

class HashTable():
  def __init__(self):
    self.data = [None] * 100

  def put(self, key, value):
    self.data[self.__hashToIndex(key)] = value

  def get(self, key):
    return self.data[self.__hashToIndex(key)]
  
  def __generateHashString(self, key):
    hashObj = hashlib.md5(key.encode())
    return hashObj.hexdigest()

  def __hashToIndex(self, key):
    hashString = self.__generateHashString(key)
    charPoints = [ord(c) for c in hashString]
    sumOfHash = sum(charPoints)
    return sumOfHash % (len(self.data) - 1)
