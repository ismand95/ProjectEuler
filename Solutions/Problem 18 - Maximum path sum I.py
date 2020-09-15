"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from
top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

                   75
                 95 64
                17 47 82
               18 35 87 10
             20 04 82 47 65
            19 01 23 75 03 34
           88 02 77 73 07 63 67
          99 65 04 28 06 16 70 92
        41 41 26 56 83 40 80 70 33
       41 48 72 33 47 32 37 16 94 29
      53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
   91 71 52 38 17 14 91 43 58 50 27 29 48
 63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
However, Problem 67, is the same challenge with a triangle containing one-hundred rows;
it cannot be solved by brute force, and requires a clever method! ;o)
"""

"""
This solution solves the problem by iteration. Because the sum is linear it must follow the maximum sum for each level
Thus the program solves every level for the maximum sum and then moves that max up 1 level.

STEP 1:
   3
  7 4
 2 4 6
8 5 9 3

STEP 2:
   3
  7 4
max(8+2, 5+2), max(5+4, 9+4), max(9+6, 3+6)

STEP 3:
   3
  7  4
10 13 15

GOTO STEP 1
"""

numbers = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

# Parse the data
# convert string of numbers to lists
numbers = numbers.strip().split('\n')

numbers = [i.replace(' ', ', ') for i in numbers]
numbers = [i.split(', ') for i in numbers]

number_dict = {}

for i, numb_list in enumerate(numbers):
    numb_list = [int(i) for i in numb_list]
    number_dict.update({i: numb_list})


def reduce_dict(numbers_collection):
    bottom_index = list(numbers_collection.keys())[-2:]
    bottom_two_lists = [numbers_collection[x] for x in bottom_index]

    possible_sums = list()  # needs to be a list of lists with the two possible sums available

    for i, j in enumerate(bottom_two_lists[0]):
        sums = []

        for k in range(2):
            sums.append(j + bottom_two_lists[1][k+i])

        # set each element in row equal to max sum between the two bottom and one top value
        possible_sums.append(max(sums))

    # set 2nd last row equal to possible sum of two last rows
    numbers_collection[bottom_index[0]] = possible_sums
    # drop the last row
    numbers_collection.pop(bottom_index[1], None)

    return numbers_collection


while len(number_dict) > 1:
    number_dict = reduce_dict(number_dict)
    print(number_dict)


print(f'The maximum path sum is: {number_dict[0][0]}')
