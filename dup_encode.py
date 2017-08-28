
# https://www.codewars.com/kata/duplicate-encoder/train/python

def duplicate_encode(word):

    encoded = ''
    word = list(word.lower())
    word = [word.count(x) for x in word]
    print(word)

    for n in word:

        if n >= 2:

            encoded += ')'

        else:

            encoded += '('

    return encoded
