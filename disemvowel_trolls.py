
# https://www.codewars.com/kata/disemvowel-trolls/train/python

import re

def disemvowel(string):
    return re.sub(r'[aeiou]','',string,flags=re.IGNORECASE)
