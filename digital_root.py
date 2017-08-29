
# https://www.codewars.com/kata/541c8630095125aba6000c00

def digital_root(num):

	while len(str(num)) > 1:

		num = sum([int(x) for x in list(str(num))])

	return num