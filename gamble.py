##
# 23/02/2026
# TS

## Slots ##

import random

# Symbols
row = ["🧠", "💎", "💰"]
column = ["🧠", "💎", "💰"]

money = int(input("How much money are you ready to risk: "))
winnings = 0



# Functions

# Making of the Grid
def generate_grid(row, column):

# Create a loop that prints random places for the symbols
    for i in range(len(row)):

    # Create a list to store the random rows to check for a win
        grid = []

    # printing slots
        for j in range(len(column)):
            random.shuffle(row)

        grid.append(row)
        return grid

while money >= 0:
    money -= 10

    # Ask user how many lines to check
    lines = int(input("what line do you want to check(1,2,3): "))

    # generating slots
    slots = generate_grid(row, column)
    print(slots)

    for r in slots:
        print(" | ".join(r))
    print()
        
# checking according to the number of lines they want to check
    for i in range(lines):

    # checking lines
        if slots[i][0] == slots[i][1] == slots[i][2]:
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
