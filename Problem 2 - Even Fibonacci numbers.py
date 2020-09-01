"""
Problem 2
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""


a = 1
b = 2
array = []

def fib(terms):
	a = 1
	b = 2
	array.append(a)
	array.append(b)

	for i in range(terms):
		c = a + b
		a = b
		b = c
		array.append(c)
fib(100)

c = []

for i in array:
	if i < 4000000 and i % 2 ==0:
		c.append(i)

print(c)
print(sum(c))
