
# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/

def find_short(s):

    return sorted([len(x) for x in s.split()])[0]