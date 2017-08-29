
# https://www.codewars.com/kata/find-the-smallest-integer-in-the-array/train/python

def findSmallestInt(arr):
    arr.sort()
    return arr[0]