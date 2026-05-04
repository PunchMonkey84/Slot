
##
#01/04/2026
#TS

##SLOTS##

import random

# Making a random grid function
def generate_grid(symbols):
    grid = []
    for i in range(3):
        row = random.choices(symbols, k=3)
        grid.append(row)
    return grid

def grid_print(grid):
    for row in grid:
        print("\t".join(row))

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

    return line.count(line[0]) == len(line)

def play(symbols):
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
        return 100
    else:
        print("You lost")
        return 0

def main():
    symbols = ["🧠", "💎", "💰"]

    winnings = 0
    winnings += play(symbols)
    print(f"You have made: ${winnings}")

if __name__ == "__main__":
    main()
