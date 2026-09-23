## Find the largest palindrome made from the product of two 3-digit numbers.
num1 = 1
limit = 99
start = 999
best = 0
for num1 in range(start, limit, -1):
    for n in range(start, limit, -1):
        number = num1 * n
        if number < best:
            break
        string1 = str(number)
        if string1 == string1[::-1]:
            best = number

print(best)
