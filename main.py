"""
main.py
Joel Bratt
Main program tic tac toe
6/26/2026
"""
import math
import random

spots = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
wincons = [
    #Horizontal
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    #Columns
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    #diag
    (0, 4, 8), (2, 4, 6)
]

def win(spots, letter):
    for combo in wincons:
        if spots[combo[0]] == letter and spots[combo[1]] == letter and spots[combo[2]] == letter:
            return True 
    return False

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

    if win(spots, xORo):
        print("you win!")
        break

    if len (openSpots) > 0:
        print("Picking spot")
        cpuLetter = "O" if xORo == "X" else "X"
        cpuChoice = random.choice(openSpots)
        spots[cpuChoice-1] = cpuLetter
        openSpots = [spot for spot in spots if isinstance(spot, int)]

    if win(spots, cpuLetter):
        print("Cpu wins!")
        break





print(  f' {spots[0]} | {spots[1]} | {spots[2]} \n'
        f'----------\n'
        f' {spots[3]} | {spots[4]} | {spots[5]} \n'
        f'----------\n'
        f' {spots[6]} | {spots[7]} | {spots[8]} \n')
print("Game Over")


