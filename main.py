"""
main.py
Joel Bratt
the main program tbd
6/26/2026
"""
import math
import random

spots = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
#is instance checks for int within spots
openSpots = [spot for spot in spots if isinstance(spot, int)]

xORo = input("Lets play Tic Tac Toe would you like to be O's or X's? ")

while xORo != "X" and xORo != "O":    
    xORo = input("That wasn't X or O input those and make sure they're capital! ")

else: print('Great lets move on\n')

while len(openSpots) > 0:

    print(f' {spots[0]} | {spots[1]} | {spots[2]} \n'
          f'----------\n'
          f' {spots[3]} | {spots[4]} | {spots[5]} \n'
          f'----------\n'
          f' {spots[6]} | {spots[7]} | {spots[8]} \n')
    
    print("Your move!\n")

    currentPick = int(input("pick an open spot at numbers 1-9: \n"))

    while spots[currentPick-1] == "X" or spots[currentPick-1] == "O":
        currentPick = int(input("pick an OPEN spot at numbers 1-9: \n"))

    spots[currentPick-1] = xORo
    openSpots = [spot for spot in spots if isinstance(spot, int)]


    if len (openSpots) > 0:
        print("Picking spot")
        cpuLetter = "O" if xORo == "X" else "X"
        cpuChoice = random.choice(openSpots)
        spots[cpuChoice-1] = cpuLetter
        openSpots = [spot for spot in spots if isinstance(spot, int)]




print(  f' {spots[0]} | {spots[1]} | {spots[2]} \n'
        f'----------\n'
        f' {spots[3]} | {spots[4]} | {spots[5]} \n'
        f'----------\n'
        f' {spots[6]} | {spots[7]} | {spots[8]} \n')
print("Game Over")


