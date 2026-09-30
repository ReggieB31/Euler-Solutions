#Find the smallest positive number evenly divisible by all numbers from 1-20
def find_smallest():
    dividend = 20
    while True:
        for i in range(20, 2, -1):
            if dividend % i != 0:
                dividend += 20
                break
        else: return dividend

print(find_smallest())