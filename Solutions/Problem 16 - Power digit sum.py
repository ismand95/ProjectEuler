"""
Problem 16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

"""

n = 2 ** 1000
n = str(n)
n_sum = 0

for number in n:
    n_sum += int(number)

print('The sum of 2 ** 1000: {0}'.format(n_sum))
