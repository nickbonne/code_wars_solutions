
# https://www.codewars.com/kata/multiples-of-3-and-5/train/python

def solution(num):
    total = 0 

    for num in range(1,num):
        if num % 5 == 0 or num % 3 == 0:
            print(num)
            total += num

    return total