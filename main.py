"""
main.py
Joel Bratt
the main program tbd
6/26/2026
"""
import math
import random

spots = [1, 2, 3, 4, 5, 6, 7, 8, 9,]

xORo = input("Lets play Tic Tac Toe would you like to be O's or X's? ")
while xORo != "X" and xORo != "O":
    xORo = input("That wasn't X or O input those and make sure they're capital! ")
else: print('Great lets move on')
print(xORo)