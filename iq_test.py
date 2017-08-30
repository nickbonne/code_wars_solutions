
# https://www.codewars.com/kata/552c028c030765286c00007d

def iq_test(numbers):

	numbers = [int(x) for x in numbers.split()]
	even_indx = []
	odd_indx = []
	indx = 0

	for i in numbers:

		if i % 2 == 0:

			even_indx.append(indx + 1)
			indx += 1

		else:

			odd_indx.append(indx + 1)
			indx += 1

	if len(even_indx) < len(odd_indx):

		return even_indx[0]

	else:

		return odd_indx[0]
