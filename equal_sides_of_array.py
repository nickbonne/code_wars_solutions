
# https://www.codewars.com/kata/5679aa472b8f57fb8c000047

def find_even_index(arr):

	arr_indx = 0

	for i in arr:

		if sum(arr[arr_indx + 1]:) == sum(arr[:arr_indx]):

			return arr_indx

		arr_indx += 1

	return -1
	