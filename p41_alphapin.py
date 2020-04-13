'''
Assignment: 4.1 Alpha Pin CIS 210 Winter 2019

Author: Derek Martin

Credits: N/A

Description: Write functions that convert between PIN numbers and pronouncable phrases.

Note: I got the program to function correctly
      however, in alphapinDecode(),
      I could not figure out how to account for the presence of a '0' in the pin.
      So, the result is the original pin missing any zeros :(
'''
import doctest
consonants = "bcdfghjklmnpqrstvwyz"
vowels = "aeiou"

def alphapinEncode(pin):
    '''
    (int) -> string

    Convert given PIN into a formatted string of consonants and vowels

    >>> alphapinEncode(4327)
    'lohi'
    >>> alphapinEncode(1298)
    'dizo'
    '''
    # doctest.testmod()
    code = ''
    while (pin != 0):
        lastTwo = pin % 100
        consonant = consonants[(lastTwo // 5)] # convert lastTwo to letters
        vowel = vowels[(lastTwo % 5)]
        code = (consonant + vowel + code) # add letters to beginning of 'code'
        # pin = (pin - lastTwo) // 100
        pin = pin // 100
    return code
    
def alphapinDecode(tone):
    '''
    (str) -> int

    Convert the formatted string back to the original PIN input from alphapinEncode()

    >>> alphapinDecode('lohi')
    4327
    >>> alphapinDecode('dizo')
    1298
    '''
    # doctest.testmod()
    if (checkTone(tone)):
        string = ''
        for i in range((len(tone) + 1) // 2):
            lastTwo = (tone[(len(tone) - 2)] + tone[(len(tone) - 1)])
            newTone = '' # Initialize temporary variable
            firstValue = lastTwo[0] # Separate last and second to last characters
            secondValue = lastTwo[1]
            for i in range(len(consonants)): # Find the index of each character
                if (consonants[i] == firstValue):
                    consonantIndex = i
            for i in range(len(vowels)):
                if (vowels[i] == secondValue):
                    vowelIndex = i
            '''
            consonantIndex = str(consonantIndex)
            vowelIndex = str(2 * vowelIndex) # Multiply vowelIndex by 2 for accurate math result
            floatVal = float(consonantIndex + "." + vowelIndex)
            twoDigits = int(floatVal * 5)
            twoDigits = str(twoDigits)
            '''
            twoDigits = (vowelIndex + consonantIndex * 5)
            if twoDigits < 10:
                twoDigits = '0' + str(twoDigits)
            twoDigits = str(twoDigits)
            string = twoDigits + string
            '''
            for i in range(len(tone) - 2): # Create a copy of tone but chop off last two characters
                newTone = newTone + tone[i]
            tone = newTone
            '''
            tone = tone[:-2]
        return string
    else:
        print("Tone is not in correct format.")
        return -1   

def checkTone(tone):
    '''
    (str) -> boolean

    Check if the argument is in the correct format (consonant then vowel)

    >>> checkTone('lohi')
    True
    >>> checkTone('olih')
    False
    '''
    # doctest.testmod()
    check = False
    for i in range(len(tone) - 1):
        if (tone[i] in consonants) and (tone[i + 1] in vowels): # check two characters at a time
            check = True
        else:
            check = False
            if (tone[i] in consonants):
                break
    return check

def main():
    ''' Function that runs Alphapin program '''
    pin = input("What number would you like to encode? ")
    pin = int(pin)
    string = alphapinEncode(pin)
    print(string)
    code = alphapinDecode(string)
    print(code)

# main()
