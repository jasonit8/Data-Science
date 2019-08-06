# This code checks whether a number is prime
def PrimeNumber(n):
    return n > 1 and all(n%i != 0 for i in range(2,int(n**.5+1)))

# Try this code on random numbers, see the result
for i in [3,39,395,3959,39595,395959,3959593,39595931,395959311,3959593117]:
    if PrimeNumber(i):
        print('%i is PRIME.' %i)
    else:
        print('%i is not prime.' %i)
# Result:
# 3 is PRIME.
# 39 is not prime.
# 395 is not prime.
# 3959 is not prime.
# 39595 is not prime.
# 395959 is PRIME.
# 3959593 is not prime.
# 39595931 is not prime.
# 395959311 is not prime.
# 3959593117 is not prime.