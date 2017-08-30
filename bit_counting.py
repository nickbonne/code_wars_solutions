
# https://www.codewars.com/kata/bit-counting/train/python

def countBits(n):

    return sum([int(x) for x in list(str(int(bin(n)[2:])))])