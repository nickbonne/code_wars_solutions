
# https://www.codewars.com/kata/your-order-please/train/python

def order(sentence):

    words = sentence.split()
    ordered = []

    for word in words:

        for letter in word:

            if letter.isdigit():

                ordered.append((word, int(letter)))

    return str(' ').join([x[0] for x in sorted(ordered, key=lambda x: x[1])])