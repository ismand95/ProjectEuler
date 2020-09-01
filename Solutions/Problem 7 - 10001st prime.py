"""
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


def is_prime(number):
    # for any integer smaller than test-number
    for k in range(number):
        # all primes > 1
        if k > 1:
            try:
                if (number % k) == 0:
                    # break loop for else exception
                    break
            except ZeroDivisionError:
                pass
    else:
        # all primes > 1
        if number > 1:
            return True
    return False


i = 1
primes = []

while True:
    if is_prime(i):
        primes.append(i)
        i += 1

        if len(primes) == 10001:
            break
    else:
        i += 1

print('10 001st prime is: {0}'.format(primes[-1]))
