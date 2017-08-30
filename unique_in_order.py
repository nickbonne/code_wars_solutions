# https://www.codewars.com/kata/unique-in-order

def unique_in_order(iterable):
    
    new = []
    last = ''

    for i in iterable:

        if i != last:

            new.append(i)
            last = i

    return new