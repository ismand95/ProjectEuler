"""
Problem 1
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

# module to time processing time
import time

# locals
start = time.time()
divisible_prime = []
target = 600851475143


def is_prime(number):
    is_prime_true = False

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
            is_prime_true = True

    # return bool on whether prime or not
    return is_prime_true


for i in range(target):
    try:
        # find any values divisible for target (without remainder)
        if target % i == 0:
            stamp = time.time()
            print('Seconds passed: {0}'.format(round(stamp - start, 2)))

            # if functions returns True on prime, append to array
            if is_prime(i):
                divisible_prime.append(i)
            print(divisible_prime)
    except ZeroDivisionError:
        pass
