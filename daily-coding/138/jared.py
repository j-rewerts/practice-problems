# Google - Hard
# Find the minimum number of coins required to make n cents.
# You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.
# For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.

def minCoins(num):
  quarters = int(num / 25)
  num = num - quarters * 25

  dimes = int(num / 10)
  num = num - dimes * 10

  nickels = int(num / 5)
  num = num - nickels * 5

  return [quarters, dimes, nickels, num]

print(minCoins(50))
print(minCoins(51))
print(minCoins(52))
print(minCoins(53))
print(minCoins(54))
print(minCoins(55))
print(minCoins(56))
print(minCoins(57))
print(minCoins(58))
print(minCoins(59))
print(minCoins(60))
print(minCoins(61))