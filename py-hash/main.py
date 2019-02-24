from hash import HashTable

def main():
  testHashToIndex()
  print("Starting with empty hash table")
  hash = HashTable()
  hash.put("A key", "a value")
  assert hash.get("A key") == "a value"
  assert hash.get("A key") != "another value"

def testHashToIndex():
  hash = HashTable()
  hashString = hash._HashTable__generateHashString('test')
  hashIndex = hash._HashTable__hashToIndex('test')
  print("Done hash test")
  

main()