"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable
numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

import numpy as np
N = 10000


def d(n):
    divisors = set()
    divisors.add(1)

    less_half = np.math.floor(n/2)

    for i in range(2, less_half + 1):

        if n % i == 0:
            divisors.add(i)

    return sum(divisors)


def is_amicable(m):
    a = d(m)
    b = d(a)

    if (m == b) and (a != b):
        return m
    else:
        return False


amicable_pairs = set()

for j in range(1, N):
    check = is_amicable(j)

    if check:
        amicable_pairs.add(j)

print(f'Sum of all the amicable numbers under {N} is {sum(amicable_pairs)}')
