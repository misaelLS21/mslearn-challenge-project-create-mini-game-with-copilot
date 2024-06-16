# write 'hello world' to the console
print('hello world')


# develop a the code for the game rock, paper scissors in python for 2 players
# get player names
player1 = input("Enter name for Player 1: ")
player2 = input("Enter name for Player 2: ")

# define the game rules
rules = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

# play the game until a winner is determined
while True:
    # get player choices
    choice1 = input(f"{player1}, enter your choice (rock, paper, scissors): ")
    choice2 = input(f"{player2}, enter your choice (rock, paper, scissors): ")

    # check if choices are valid
    if choice1 not in rules or choice2 not in rules:
        print("Invalid choice. Please try again.")
        continue

    # determine the winner
    if choice1 == choice2:
        print("It's a tie!")
    elif rules[choice1] == choice2:
        print(f"{player1} wins!")
        break
    else:
        print(f"{player2} wins!")
        break