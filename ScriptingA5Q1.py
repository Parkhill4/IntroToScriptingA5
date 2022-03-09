"""
        Question 1: This program will accept a string and
                    convert it to morse code
"""
def strToMorse(string):
    morseDict = {' ': '|', 'A': '.-', 'B': '-...','C': '-.-.',
    'D': '-..','E': '.','F': '..-.','G': '--.','H': '....',
    'I': '..','J': '.---','K': '-.-','L': '.-..',
    'M': '--','N': '-.','O': '---','P': '.--.',
    'Q': '--.-','R': '.-.','S': '...','T': '-',
    'U': '..-','V': '...-','W': '.--','X': '-..-',
    'Y': '-.--','Z': '--..', '0': '-----', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..'}

    morse_code = ""

    for i in string:
        morse_code += morseDict[i.upper()]

    return morse_code

string = input("Enter text to be converted: ")
print(strToMorse(string))
