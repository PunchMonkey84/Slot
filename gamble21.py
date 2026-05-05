##
#01/04/2026
#TS

##SLOTS##

import random

# Making a random grid function
def generate_grid(symbols):
    grid = []
    for _ in range(3):
        row = [random.choice(symbols) for _ in range(3)]
        grid.append(row)
    return grid

def grid_print(grid):
    for row in grid:
        print("\t".join(row))

# Checking the line they want checked function
def checking(grid, check):
    if check == 1:
        line = grid[0]
        print("Checking row 1: {}".format(line))
    elif check == 2:
        line = grid[1]
        print("Checking row 2: {}".format(line))
    elif check == 3:
        line = grid[2]
        print("Checking row 3: {}".format(line))
    elif check == 4:
        line = [grid[0][0], grid[1][1], grid[2][2]]
        print("Checking diagonal: {}".format(line))
    elif check == 5:
        line = [grid[0][2], grid[1][1], grid[2][0]]
        print("Checking diagonal: {}".format(line))
    else:
        print("Input a valid choice!")
        return False

    # Check if all symbols in the line are the same
    if line.count(line[0]) == 3:
        return True

    return False

def play(symbols):
    winnings = 0

    # Ways slots can be checked
    print("""
1. First row
2. Second row
3. Third row
4. Diagonal from left bottom to right top
5. Diagonal from right bottom to left top
""")

    # Ask the user what way they want slot to be checked
    check = int(input("Please choose the way you want the slots to be checked (1-5): "))

    # Making the slot machine
    slots = generate_grid(symbols)

    # Printing Slot machine
    grid_print(slots)
    print()

    # See if the user won and tell them
    victory = checking(slots, check)

    if victory:
        print("You won!")
        winnings += money + 100
    else:
        money -= 10
        print("You lost")

    return winnings

def main():
    money = int(input("How much money are you betting for $100: "))
    symbols = ["🧠", "💎", "💰"]
    winnings += play(symbols)
    print(f"You have made: ${winnings}")

if __name__ == "__main__":
    main()
