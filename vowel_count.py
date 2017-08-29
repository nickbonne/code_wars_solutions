
# https://www.codewars.com/kata/54ff3102c1bad923760001f3

def getCount(inputStr):

	num_vowels = 0
	vowels = ['a', 'e', 'i', 'o', 'u']

	for c in list(inputStr):

		if c in vowels:

			num_vowels += 1

    return num_vowels
