
# https://www.codewars.com/kata/find-maximum-and-minimum-values-of-a-list/train/python

def min(arr):
    arr.sort()
    return arr[0]


def max(arr):
    arr.sort()
    return arr[-1]