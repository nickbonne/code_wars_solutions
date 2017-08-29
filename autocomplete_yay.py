
# https://www.codewars.com/kata/autocomplete-yay/train/python

import re

def autocomplete(input_, dictionary):

    input_ = re.sub(r'[^a-zA-Z]', r'', input_)
    matches = []

    for i in dictionary:

        i_fixed = re.sub(r'[^a-zA-Z]', r'', i)

        if re.match(input_.lower(), i_fixed.lower()):

            matches.append(i)

    return matches[:5]