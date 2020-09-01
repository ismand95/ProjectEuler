"""
Problem 4
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(number):
    # read number as string backwards and compare to number as string.
    # read using advanced slicers
    if str(number) == str(number)[::-1]:
        return True
    else:
        return False


def find_palindrome_in_range(start, stop):
    # use is_palindrome() to append array with palindromes from range
    array = []
    for k in range(start, stop + 1):
        if is_palindrome(k):
            array.append(k)
    return array


array = find_palindrome_in_range(10000, 998001)

# dictionary to hold results
return_values = {'a': [], 'b': [], 'c': []}


def main(palin_array):
    for i in palin_array:
        for j in range(100, 999):
            if i % j == 0 and (i / j) <= 999:
                return_values['a'].append(i)
                return_values['b'].append(j)
                return_values['c'].append(i / j)

    # find highest palindrome which is a product of xXx x xXx
    idx = return_values['a'].index(max(return_values['a']))

    multiple1 = int(return_values['c'][idx])
    multiple2 = int(return_values['b'][idx])
    result = int(return_values['a'][idx])

    return multiple1, multiple2, result


print('{0} x {1} = {2}'.format(main(array)[0],
                               main(array)[1],
                               main(array)[2]))
