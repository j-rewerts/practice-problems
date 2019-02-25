# Cracking the coding interview 17.6
# @author CodyGramlich and j-rewerts
# Count the number of 2s on the way to a number
import math

def getMajor(num):
    x = math.floor(math.log(num, 10))
    value = x * math.floor(num / math.pow(10, x)) * math.pow(10, x) / 10
    modifiedNum = num - 2*math.pow(10, x) + 1
    value += min(max(modifiedNum, 0), math.pow(10, x))
    return value

def get2s(num):
    value = 0
    while num > 0:
        x = math.floor(math.log(num, 10))
        value += getMajor(num)
        num = num % math.pow(10, x)
    return value

print(get2s(735))
print(get2s(25))