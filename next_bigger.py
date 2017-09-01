
 #https://www.codewars.com/kata/next-bigger-number-with-the-same-digits/train/python

def next_bigger(n):

    n = str(n)

    # if numbers are sorted in desccending order
    if int(n) == int(''.join(sorted([x for x in n], reverse=True))):

        return -1

    # if numbers are in ascending order
    elif int(n) == int(''.join(sorted([x for x in n]))) and \
        n[-2] != n[-1]:

        return int(n[:-2] + n[-2:][::-1])

    # if numbers has len of 2, if reversed > n
    elif len(n) == 2:

        if int(''.join(n[::-1])) > int(n):

            return int(''.join(n[::-1]))

        else:

            return -1

    last_d = n[-1]
    passed = last_d

    for digit in n[:-1][::-1]:

        if digit < last_d:

            tail = digit + passed
            tail_set = set(tail)
            big_num = set([str(x) for x in range(int(tail[0]), 10)])
            big_num = sorted(list(big_num & tail_set))[:2]

            tail = [x for x in tail]
            big_num_index = [tail.index(x) for x in big_num]
            tail.pop(0)
            del tail[big_num_index[1] - 1]
            tail.insert(0, big_num[1])
            tail.insert(big_num_index[1], big_num[0])
            tail_2 = sorted(tail[1:])
            tail = ''.join(list(tail[0]) + tail_2)
            return int(n[:-(len(str(tail)))] + tail)

        else:

            last_d = digit
            passed = digit + passed

    return -1

