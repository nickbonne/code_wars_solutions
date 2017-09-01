
def sum_pairs(ints, s):

    seen = {}

    for n, i in enumerate(ints):

        diff = s - i

        if diff in seen.keys():

            return [diff, seen[diff]]

        else:

            seen[i] = diff

    return None
