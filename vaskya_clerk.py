
# https://www.codewars.com/kata/vasya-clerk/train/python

def tickets(people):

    count25 = 0
    count50= 0
    count100 = 0
    change = False

    if people[0] != 25:
        return 'NO'

    count25 =  1

    for person in people[1:]:

        if person == 25:
            count25 += 1
            change = True

        elif person == 50:
            if count25 >= 1:
                change = True
                count25 -= 1
                count50 += 1

            else:
                change = False

        elif person == 100:
            if count50 >= 1 and count25 >= 1:
                change = True
                count25 -= 1
                count50 -= 1
                count100 += 1
            elif count25 >= 3:
                change = True
                count25 -= 3
                count100 += 1
            else:
                change = False

    if change:
        return 'YES'
    else:
        return 'NO'
