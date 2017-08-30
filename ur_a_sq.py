
# https://www.codewars.com/kata/youre-a-square/train/python

def is_square(apositiveint):
    if apositiveint < 0:
        return False
    x = apositiveint // 2
    seen = set([x])
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen: return False
        seen.add(x)
    return True
