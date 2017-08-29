
# https://www.codewars.com/kata/stop-gninnips-my-sdrow/train/python

def spin_words(sentence):

    new_sentence = []
    for word in sentence.split():

        if len(word) >= 5:
            new_sentence.append(''.join(list(reversed(word))))
        else:
            new_sentence.append(word)

    return " ".join(new_sentence)