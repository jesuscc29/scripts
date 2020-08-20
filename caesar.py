#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" Caesar's cipher script.

Script that encrypt messages using Caesar's cipher with the below indications:

* The program must accept a single command-line argument, non-negative integer.
* If program is executed without any command-line arguments or with more than 
  one command-line argument, should print an error message and exit immediatly.
* Script should work for all non-negative integers values of K less than 
  231 - 26. 
"""

__author__ = 'Jesús Antonio Cota Cota'
__email__ = 'jesuscota991@gmail.com'

import sys


if len(sys.argv) == 2:
    # Getting steps to use on cipher on first argument value.
    steps = int(sys.argv[1])
    # Input to receive from user.
    plaintext = input('plaintext: ')
    # Output variable.
    output = ''

    # Loop each character from user input.
    for i in plaintext:
        # Validate if is alphanumeric char, otherwise just pass it like that.
        if i.isalpha():
            # Discriminate upper and lowe case, they need to keep it's 'case'.
            if i.isupper():
                # Get int representation of char, then 'increment' the steps
                # and substract the initial ascii position of upper/lower case 
                # alphabet representation.
                # Do a modulus of 26 (all valid alphabet positions) from the
                # previuous result, then increment the initial ascii 
                # position again to have the final value, then use 'chr'
                # to have the str representation of the value.
                output += chr((ord(i) + steps - 65) % 26 + 65)
            else:
                output += chr((ord(i) + steps - 97) % 26 + 97)
        else:
            output += i

    # Output the final value.
    print('ciphertext: ', output)
else:
    # Show error on bad arguments.
    print('Error, you should put one argument.')
    sys.exit(1)
