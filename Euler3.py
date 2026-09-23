## What is the largest prime factor of the number 600851475143

"""
Loop over all numbers under limit.
Check if each number is prime. 
"""
prime = 0
orig = 600851475143
limit = int(600851475143 ** 0.5)


for n in range(2, limit):
    if orig % n == 0:
        for a in range(2, n):
            if n % a == 0:
                break
        else:
            prime = n
print(prime)
                    
