
# https://www.codewars.com/kata/consecutive-strings

def longest_consec(strarr, k):

    place = 0
    pairs = []

    if len(strarr) == 0 or len(strarr) < k or k <= 0:

        return ""

    for el in strarr:

        if place <= len(strarr) - k:

            pairs.append(strarr[place:place + k])
            place += 1

    solution = sorted([(''.join(x), len(''.join(x))) for x in pairs],
            key=lambda x: x[1], reverse=True)[0][0]

    return solution


    

print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3))