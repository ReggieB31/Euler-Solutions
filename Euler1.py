## Find the sum of all multiples of 3 or 5 below 1000

"""
Loop over all numbers below 1000, check if each are divisible by 3 or 5.
Continuosly append all numbers divisible by either to the sum.
"""

sum = 0

for i in range(1000):
    if (i % 5 == 0) or (i % 3 == 0):
        sum += i

print(sum)