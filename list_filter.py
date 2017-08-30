
# https://www.codewars.com/kata/list-filtering/train/python

def filter_list(l):
	new_list = [v for v in l if isinstance(v,int)]
	return new_list
