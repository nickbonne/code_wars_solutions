
# https://www.codewars.com/kata/5884b6550785f7c58f000047

def group(arr):

	solution = []
	new_arr = []
	counted = [(x, arr.count(x)) for x in arr]

	for x in counted:

		if x not in new_arr:

			new_arr.append(x)

	for y in new_arr:

		solution.append([y[0] for x in range(y[i])])

	return solution
