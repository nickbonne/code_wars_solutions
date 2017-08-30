
# https://www.codewars.com/kata/54b724efac3d5402db00065e

decodeMorse(morseCode):

   solution = ''
    
    if len(morseCode.split('  ')) == 1:
    
        return ''.join([MORSE_CODE[char] for char in morseCode.split()])
    
    for item in morseCode.split('  '):
    
        for char in item.split():
        
            if char == item.split()[-1]:

                solution = solution + MORSE_CODE[char] + ' '
                
            else:

                solution = solution + MORSE_CODE[char]

    return solution.strip()