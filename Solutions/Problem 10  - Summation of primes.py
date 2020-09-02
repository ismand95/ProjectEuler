"""
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import numpy as np

# below is example with Fermat's small theorem - which works, but is slow...


def fermat_primality(number, runs):
    main = []

    def fermat_test(n):
        x = np.random.randint(2, n - 2)
        t = x ** (n - 1)

        if t % n == 1:
            return True
        else:
            return False

    for i in range(runs):
        if fermat_test(number):
            main.append(True)
        else:
            main.append(False)

    if False in main:
        return False

    return True


def execute_fermat(n):
    fermat_primes = [2, 3]

    for j in range(5, n + 1):
        if fermat_primality(number=j, runs=2):
            fermat_primes.append(j)
            print(j)


# execute_fermat(2000000)


# implementation of Sieve of Eratosthenes - much more efficient

def sieve_of_eratosthenes(n):
    # set can only contain unique values
    non_primes = set()
    primes = set()

    for i in range(2, n + 1):  # run numeral n (n + 1) because 0 count
        # sets are efficient for lookups like below

        if i not in non_primes:

            # do sieve cross-out with distance i and start i^2, end numeral n
            non_primes.update(range(i**2, n + 1, i))

            # add i to primes, because it hasn't been crossed yet, and must be prime
            primes.add(i)

    # return sorted set of primes
    return sorted(primes)


print(sum(sieve_of_eratosthenes(2000000)))
