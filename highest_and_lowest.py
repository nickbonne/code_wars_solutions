
# https://www.codewars.com/kata/554b4ac871d6813a03000035

def high_and_low(numbers):

	numbers = sorted([int(x) for x in numbers.split()])

	return str(numbers[-1]) + " " + str(numbers[0])
