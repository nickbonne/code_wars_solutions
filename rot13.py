
# https://www.codewars.com/kata/530e15517bc88ac656000716/

def rot13(message):

    encoded = ""

    message = [ord(x) for x in message]
    print(message)

    for num in message:

        if num > 64 and num < 91:

            if num < 78:

                encoded = encoded + chr(num + 13)

            else:

                num = (12 - (90 - num)) + 65
                encoded = encoded + chr(num)

        elif num > 96 and num < 123:

            if num < 110:

                encoded = encoded + chr(num + 13)

            else:

                num = (12 - (122 - num)) + 97
                encoded = encoded + chr(num)

        else:

            encoded = encoded + chr(num)

    return encoded
    