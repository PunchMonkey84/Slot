##
#01/04/2026
#TS

##SLOTS##

import random

# Making a random grid function
def generate_grid(symbols):
    grid = []
    return grid

def grid_print(grid):
    for row in grid:
        print("/t".join(row))

# Checking the line they want checked function
def checking(grid, check):
    if check == 1:
        line = grid[0]
        print(f"Checking row 1: {line}")
    elif check == 2:
        line = grid[1]
        print(f"Checking row 2: {line}")
    elif check == 3:
        line = grid[2]
        print(f"Checking row 3: {line}")
    elif check == 4:
        line = [grid[0][0], grid[1][1], grid[2][2]]
        print(f"Checking diagonal: {line}")
    elif check == 5:
        line = [grid[0][2], grid[1][1], grid[2][0]]
        print(f"Checking diagonal: {line}")
    else:
        print("Input a valid choice!")
        return False

    return False

def play():
    # Ways slots can be checked
    print("""
1. First row
2. Second row
3. Third row
4. Diagonal from left bottom to right top
5. Diagonal from right bottom to left top
""")

# Ask the user what way they want slot to be checked
    check = int(input(" Please choose the way you want the slots to be checked (1-5): "))

# Making the slot machine
    slots = generate_grid(symbols)
# Printing Slot machine
    for sym in slots:
        print(" | ".join(sym))
    print()

# See if the user won and tell them
    victory = checking(slots, check)

    if victory:
        print("You won!")
        winnings += 100
    else:
        print("You lost")

def main():
    symbols = ["🧠", "💎", "💰"]

    winnings = 0
    winnings += play(symbols)
    print(f"You have made: ${winnings}")


if __name__ == "__main__":
    main()
