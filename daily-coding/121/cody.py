def canBePalindrome(k, word):
    start = 0
    end = len(word) - 1
    
    def deleteIsPalindrome(word, k, start, end):
        while end - start >= 1:
            if word[start] != word[end]:
                if k == 0:
                    return False
                if not deleteIsPalindrome(word, k - 1, start + 1, end) and not deleteIsPalindrome(word, k - 1, start, end - 1):
                    return False
            start += 1
            end -= 1
        return True
    
    return deleteIsPalindrome(word, k, start, end)

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