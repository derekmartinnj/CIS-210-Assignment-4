'''
Project: Assingment 4.2 Binary CIS 210 Winter 2019

Author: Derek Martin

Credits: https://www.electronics-tutorials.ws/binary/bin_2.html

Description: Write functions to encode and decode decimal to binary representations of numbers.
'''
import doctest

def dtob(n):
    '''
    (int) -> str

    Convert given 'int' into binary code

    >>> dtob(27)
    '11011'
    >>> dtob(0)
    '0'
    '''
    #print(doctest.testmod())
    binary = ''
    if n == 0: # account for '0' input
        return str(0)
    while (n > 0):
        binary = str(n % 2) + binary
        n = n // 2
    return str(binary)

def btod(b):
    '''
    (str) -> int

    Convert given binary 'string' into the integer it represents

    >>> btod('0000')
    0
    >>> btod('1101')
    13
    '''
    #print(doctest.testmod())
    number = 0
    for i in b:
        number = number * 2
        number += int(i)
    return number

def main():
    ''' '''
    nonNeg = int(input("Enter non-negative integer: ")) # protect code (make sure it's an int)
    print("Binary format is", dtob(nonNeg))
    print("Back to decimal:", btod(dtob(nonNeg)))

main()
