"""
Problem 15

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

**** SEE PICTURES ON PROJECTEULER.COM ****

How many such routes are there through a 20×20 grid?

"""

import numpy as np

'''
uses simple combinations formula of statistics:

combinations = n! / (k! * (n - k)!)

'''

moves = 40  # 20 D, 20 R
R = 20
D = 20  # unused

comb = np.math.factorial(moves)/(np.math.factorial(R) * np.math.factorial(moves - R))

print('number of Lattice paths to corner: {0}'.format(int(comb)))
