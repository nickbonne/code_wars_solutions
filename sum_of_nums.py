
# https://www.codewars.com/kata/beginner-series-number-3-sum-of-numbers/train/python

def get_sum(a,b):
    lst = [a,b]
    lst.sort()
    return sum(range(lst[0],lst[1]+1))
