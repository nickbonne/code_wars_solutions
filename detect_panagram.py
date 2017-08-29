
# https://www.codewars.com/kata/detect-pangram/train/python

import string

def is_pangram(s):
     return not set('abcdefghijklmnopqrstuvwxyz') - set(s.lower())