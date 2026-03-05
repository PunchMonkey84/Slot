##
# 23/02/2026
# TS

## Slots ##

import random

# Symbols
row = ["\U0001F911", "💎", "💰"]
column = ["\U0001F911", "💎", "💰"]

money = int(input("How much money are you ready to risk: "))
winnings = 0

while money >= 0:
    money -= 10
# ask user how much lines to check
    lines = int(input("what line do you want to check(1,2,3): "))

# Create a loop that prints random places for the symbols
    for i in range(len(row)):
    
    # Create a list to store the random rows to check for win
        wose = []

    # printing slots
        for j in range(len(column)):
            random.shuffle(row)
            wose.append(row[0])
            print((row[0]), end ="   ")
        print()

# checking according to the amount of lines they want to check
    for k in range(lines):

    # checking lines
        if wose[0] == wose[1] == wose[2]:
            win = True
            winnings += 100
            
        else:
            win = False

# Tell them if they won or not
    if win == True:
        print("you won")
    else:
        print("you lost")

# display how much they have left
print("You have won ${}".format(winnings))


