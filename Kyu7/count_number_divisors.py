# Count the number of divisors of a positive integer n.

# Random tests go up to n = 500000.

# Examples
# divisors(4)  == 3  # 1, 2, 4
# divisors(5)  == 2  # 1, 5
# divisors(12) == 6  # 1, 2, 3, 4, 6, 12
# divisors(30) == 8  # 1, 2, 3, 5, 6, 10, 15, 30

import math, operator, time
from functools import reduce

def find_primes(num):
    arr = []
    while num % 2 == 0:
        # print(2)
        arr.append(2)
        num /= 2
    
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            # print(i)
            arr.append(i)
            num /= i

    if num > 2:
        arr.append(int(num))
        
    return arr

def custom_prod(itera):
    return reduce(operator.mul, itera, 1)


def divisors(n):
    array = find_primes(n)
    counts = {x: array.count(x) for x in array}
    arr = []
    for key in counts:
        arr.append(counts[key] + 1)
    # return math.prod(arr) Python 3.8+
    return custom_prod(arr)

print(divisors(4)) # 1, 2, 4
print(divisors(5)) # 1, 5
print(divisors(12)) # 1, 2, 3, 4, 6, 12
print(divisors(30)) # 1, 2, 3, 5, 6, 10, 15, 30