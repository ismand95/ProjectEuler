"""
Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115(one hundred and fifteen) contains 20 letters.

The use of "and" when writing out numbers is in compliance with British usage.
"""

numb_collection = {
    'ones': {
        0: '',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'
    },
    'tens': {
        0: '',
        1: 'ten',
        2: 'twenty',
        3: 'thirty',
        4: 'forty',
        5: 'fifty',
        6: 'sixty',
        7: 'seventy',
        8: 'eighty',
        9: 'ninety'
    },
    'teens': {
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen'
    }
}


def number_letter_count(n):
    def ones(one):
        return numb_collection['ones'].get(one)

    def tens(ten):
        return numb_collection['tens'].get(ten)

    # teens are special - we'll catch those early on
    if numb_collection['teens'].get(n) is not None:
        return numb_collection['teens'].get(n)

    # thousand
    if n == 1000:
        return 'onethousand'

    n = [int(x) for x in str(n)]  # convert number to string

    numb_str = ones(n[-1])

    if len(n) > 1:
        numb_str = tens(n[-2]) + numb_str

    if len(n) > 2:
        if sum(n[1:]) == 0:
            numb_str = ones(n[0]) + 'hundred'
        elif n[1] == 1 and n[2] > 0:
            numb_str = ones(n[-3]) + 'hundredand' + numb_collection['teens'].get(int(str(n[1]) + str(n[2])))
        else:
            numb_str = ones(n[-3]) + 'hundredand' + numb_str

    return numb_str


j = int()

for i in range(1, 1001, 1):
    j += len(number_letter_count(i))
    print(number_letter_count(i))

print(j)
