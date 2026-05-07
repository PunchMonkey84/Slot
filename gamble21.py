"""slot machine.py."""
# 01/04/2026
# TS

# SLOTS##

import random

# Constants
losing_amount = 10
winning_amount = 100
maximum_lifetime_losses = 500


# Making a random grid function
def generate_grid(symbols):
    """Return the slot machine grid."""
    grid = []
    for _ in range(3):
        row = [random.choice(symbols) for _ in range(3)]
        grid.append(row)
    return grid


def grid_print(grid):
    """Print the slot machine grid."""
    for row in grid:
        print("\t".join(row))


# Checking the line they want checked function
def checking(grid, check):
    """Check according to the user's liking."""
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


# Whale check function
def check_marketing_status(profile):
    """Check if player is a whale."""
    if profile["lifetime_losses"] > maximum_lifetime_losses:
        print("Buy more credits!")
        profile["target_ads"] = True

    else:
        print("Keep playing to climb the leaderboard!")


def play(symbols, money, profile):
    """Check if they won or not."""
    winnings = 0
    score = 0

    # Playing until users wants to stop
    repeat = True
    while repeat:

        # Ways slots can be checked
        print("""
1. First row
2. Second row
3. Third row
4. Diagonal from left bottom to right top
5. Diagonal from right bottom to left top
""")

        # Ask the user what way they want slot to be checked
        check = int(input("Choose ways to be checked (1-5): "))

        # Making the slot machine
        slots = generate_grid(symbols)

        # Printing Slot machine
        grid_print(slots)
        print()

        # See if the user won and tell them
        victory = checking(slots, check)

        if victory:
            print("You won!")
            winnings += money + winning_amount
            score += winning_amount

            # Update high score
            if score > profile["high_score"]:
                profile["high_score"] = score

        else:
            money -= losing_amount
            profile["lifetime_losses"] += losing_amount
            print("You lost")

        # Checking the whale status
        check_marketing_status(profile)

        again = input("Do you want to play again? y/n: ")

        if again == "y":
            repeat = True
        elif again == "n":
            repeat = False
        else:
            print("Enter y/n next time! Goodbye for now")

    return winnings


# Players info
all_players = [
    {"name": "Ruby", "location": "Auckland",
     "high_score": 120, "lifetime_losses": 4, "target_ads": False},
    {"name": "Saba", "location": "Wellington",
     "high_score": 90, "lifetime_losses": 0, "target_ads": True},
    {"name": "Polly", "location": "Auckland",
     "high_score": 150, "lifetime_losses": 8, "target_ads": False},
    {"name": "Stacy", "location": "Dunedin",
     "high_score": 60, "lifetime_losses": 17, "target_ads": False}
]


def players(player_profile):
    """Profile menu."""
    print("""
1. To see everyone's high scores
2. To see top player to beat
3. To update details
4. To continue to the game
""")

    # Ways user can see Profiles
    choice = input("Choose option: ")

    # View all players
    if choice == "1":
        for player in all_players:
            print(f"{player['name']} - {player['high_score']}")

    # View top player
    elif choice == "2":
        if len(all_players) > 0:
            top_player = all_players[0]

            for player in all_players:
                if player["high_score"] > top_player["high_score"]:
                    top_player = player

            print(f"{top_player['name']} with score of"
                  f"{top_player['high_score']}")

    # Update existing player
    elif choice == "3":

        player_profile["name"] = input("Enter new name: ")
        player_profile["location"] = input("Enter new location: ")

        print("Details updated to {}".format(player_profile))

    # Continue the game
    elif choice == "4":
        return

    # Invaild option
    else:
        print("Invalid choice.")


def main():
    """Run the Slot machine."""
    # Profile details
    winnings = 0
    name = input("Enter your name: ").title()
    location = input("Enter location(optional): ").title().strip()

    # Crash-proofing
    while True:
        try:
            money = int(input("How much money are you betting for $100: "))
            break
        except ValueError:
            print("Enter a valid number!")

    # Symbols in the grid
    symbols = ["🧠", "💎", "💰"]

    # Player profile
    player_profile = {
        "name": name,
        "location": location,
        "high_score": 0,
        "lifetime_losses": 0,
        "target_ads": False
    }

    # Calculating the win
    winnings += play(symbols, money, player_profile)

    print(f"You have made: ${winnings}")

    # Top scores and profile details
    check_marketing_status(player_profile)
    players(player_profile)


if __name__ == "__main__":
    main()
