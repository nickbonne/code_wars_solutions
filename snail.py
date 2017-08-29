# https://www.codewars.com/kata/snail

def snail(array):

    if len(array) == 1:

        return array[0]

    height = len(array)
    width = len(array[0])

    snail_sort = array[0]

    for row in array[1:-1]:

        snail_sort.append(row[width - 1])

    for num in array[-1][::-1]:

        snail_sort.append(num)

    r = -2
    c = 0
    height -= 2
    width -= 2

    while height > 0:

        break

        for i in range(height):

            r -= 1
            snail_sort.append(array[r][c])

        for i in range(width):

            snail_sort.append(array[r][c])

        for i in range(height):

            r +=1
            snail_sort.append(array[r][c])

        for i in range(width):

            c -= 1
            snail_sort.append(array[r][c])

        break

    return snail_sort


array = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10,11,12],
         [13,14,15,16]]

array_2 = [[1,2,3],
         [4,5,6],
         [7,8,9]]

array_3 = [[1,  2,  3,  4,  5],
           [6,  7,  8,  9,  10],
           [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25]]

array_4 = [[1,  2,  3,  4,  5,  6],
           [7,  8,  9, 10, 11, 12,],
           [13, 14, 15, 16, 17, 18],
           [19, 20, 21, 22, 23, 24],
           [25, 26, 27, 28, 29, 30],
           [31, 32, 33, 34, 35 ,36]]

print(snail(array_4))