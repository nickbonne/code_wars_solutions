
# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec

def persistence(num):

	iterations = 0

	while len(str(num)) > 1:

		product = 1
		iterations += 1

		for i in [int(x) for x in list(str(num))]:

			product *= i
			num = product

	return iterations
