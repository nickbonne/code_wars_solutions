
# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039

def mumbling(s):

	count = 1
	strings = []

	for i in s:

		i = i * count
		strings.append(i.capitalize())
		count += 1

	return "-".join(strings)
