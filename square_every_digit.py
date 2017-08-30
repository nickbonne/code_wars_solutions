
# https://www.codewars.com/kata/square-every-digit

def square_digits(num):
    
    square_list =  [(x*x) for x in [int(i) for i in list(str(num))]]

    return int(''.join(str(x) for x in square_list))
