
 # https://www.codewars.com/kata/playing-with-digits/train/python

def dig_pow(n, p):

    result = zip(
            [int(x) for x in str(n)],
            [x for x in range(p, p + (len(str(n))))]
            )
    result = sum([x[0] **x[1] for x in list(result)])

    if result % n == 0:

        return int(result / n)

    else:

        return -1

