
# https://www.codewars.com/kata/factorial-1/train/python

def factorial(n):

    nums = range(1, n + 1)

    ans = 1

    for num in nums:

        ans = ans * num

    return ans