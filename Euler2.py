## By considering the terms in the Fibonacci sequence 
# whose values do not exceed four million, find the sum of the even-valued terms.

limit = 4000000
lead, second = 1, 0
total = 0
while True:
    num = lead + second
    if num > limit:
        break
    if num % 2 == 0:
        total += num
    second, lead = lead, num
    
print(total)
     