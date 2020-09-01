"""
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def find_identity_values():
    sum_py = 1000

    for a in range(1, int(sum_py/3)):
        for b in range(a + 1, int(sum_py/2)):
            c = sum_py - a - b

            if a*a + b*b == c*c:
                return a * b * c

    return False


print('\nProduct of abc is: {0}'.format(find_identity_values()))
