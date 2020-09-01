"""
Problem 14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""


def collatz_even(n):
    return int(n / 2)


def collatz_odd(n):
    return int((3 * n) + 1)


def collatz_loop(n):
    iteration = list()
    while n != 1:
        if n % 2 == 0:
            n = collatz_even(n)
        else:
            n = collatz_odd(n)

        iteration.append(n)
    return len(iteration) + 1


longest = {'n': 0,
           'i': 0}

for i in range(2, 1000000):
    q = collatz_loop(i)
    if q > longest['n']:
        longest['n'] = q
        longest['i'] = i
        print('the longest chain so far: {0}'.format(longest))


