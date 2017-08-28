
# https://www.codewars.com/kata/directions-reduction/train/python

def dirReduc(arr):

    final = []
    # compass dict
    c = {}
    c['NORTH'] = 'SOUTH'
    c['SOUTH'] = 'NORTH'
    c['EAST'] = 'WEST'
    c['WEST'] = 'EAST'

    for i in arr:

        if final and final[-1] == c[i]:

            final.pop()

        else:

            final.append(i)


    return final
