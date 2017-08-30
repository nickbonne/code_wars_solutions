
# https://www.codewars.com/kata/especially-joyful-numbers/train/python

def numberJoy(n):
    n_sum = sum([int(i) for i in list(str(n))])
    
    if n % n_sum == 0:
        if n_sum * int(str(n_sum)[::-1]) == n:
            return True
        else:
            return False
            
    else:
        return False