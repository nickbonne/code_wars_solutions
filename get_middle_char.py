
# https://www.codewars.com/kata/get-the-middle-character/train/python

def get_middle(s):
    s_len = len(s)
    mid = int(s_len / 2)

    if s_len % 2 == 0:
        return s[mid-1:mid+1]
    
    else:
        return s[mid]