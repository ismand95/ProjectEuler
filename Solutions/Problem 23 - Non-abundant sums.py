"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant
if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum
of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two
abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that
the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

import numpy as np

# all numbers over this can be written as sums of abundant numbers
limit = 28123


def d(n):
    divisors = set()
    divisors.add(1)

    less_half = np.math.floor(n / 2)

    for i in range(2, less_half + 1):

        if n % i == 0:
            divisors.add(i)

    return sum(divisors)


def all_abundant():
    abundant = list()

    for i in range(12, limit + 1):
        if d(i) > i:
            abundant.append(i)

    return abundant


abundant_numbers = all_abundant()

# Sieve like algorithm to zero out all numbers that can be written as the sum of abundant numbers
# then take the sum of the remaining
rang = [x for x in range(0, limit)]

for i in abundant_numbers:
    for j in abundant_numbers:
        if (i + j) < limit:
            # print(i+j)
            rang[i + j] = 0
        else:
            break

print(f'The sum of positive integers that cannot be written as the sum of two abundant numbers is: {sum(rang)}')
