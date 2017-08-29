
# https://www.codewars.com/kata/5467e4d82edf8bbf40000155

def descending_order(num):

	return int("".join([str(i) for i in
		                sorted([int(x) for x in list(str(num))]
		                	    reverse=True)]))
