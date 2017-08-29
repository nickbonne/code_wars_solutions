
# https://www.codewars.com/kata/5526fc09a1bbd946250002dc

def find_outlier(integers):

	even_indx = []
	odd_indx = []

	for i in integers:

		if i % 2 == 0:

			even_indx.append(i)

		else:

			odd_indx.append(i)

	if len(even_indx) < len(odd_indx):

		return even_indx[0]

	else:

		return odd_indx[0]
