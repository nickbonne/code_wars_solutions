
# https://www.codewars.com/kata/find-the-odd-int/train/python

def find_it(seq):

    for i in seq:

        if seq.count(i) % 2 != 0:

            return i