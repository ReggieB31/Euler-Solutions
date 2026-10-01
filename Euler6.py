#Find the difference between sum of squares and square of sum.

#Find sum of squares
sqr_sum = 0
for num in range(1, 101):
    sqr_sum += num ** 2
#Find square of sum
sum_sqrd = 0
for num in range(1, 101):
    sum_sqrd += num
sum_sqrd *= sum_sqrd

#Find diff
print(answer := sum_sqrd - sqr_sum)